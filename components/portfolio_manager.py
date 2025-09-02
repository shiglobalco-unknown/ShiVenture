#!/usr/bin/env python3
"""
Multi-Account Portfolio Manager
Track multiple TopStep accounts and prepare for copy trading across 5x150K accounts
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
from typing import Dict, List, Any
import json
import uuid


class Account:
    """Individual account representation"""
    def __init__(self, account_id: str, account_type: str, account_size: float, status: str = "Active"):
        self.account_id = account_id
        self.account_type = account_type  # "50K_COMBINE", "150K_COMBINE", "FUNDED", "PRIVATE"
        self.account_size = account_size
        self.status = status  # "Active", "Inactive", "Funded", "Failed"
        self.current_balance = account_size
        self.daily_pnl = 0.0
        self.total_pnl = 0.0
        self.positions = []
        self.trade_history = []
        self.max_drawdown = 0.0
        self.profit_target = self._get_profit_target()
        self.daily_loss_limit = self._get_daily_loss_limit()
        self.created_date = datetime.now()
        self.last_updated = datetime.now()
        
    def _get_profit_target(self) -> float:
        """Get profit target based on account type"""
        targets = {
            "50K_COMBINE": 3000.0,
            "100K_COMBINE": 6000.0,
            "150K_COMBINE": 9000.0,
            "FUNDED": 0.0,  # No target for funded
            "PRIVATE": 0.0  # No target for private
        }
        return targets.get(self.account_type, 0.0)
    
    def _get_daily_loss_limit(self) -> float:
        """Get daily loss limit based on account type"""
        limits = {
            "50K_COMBINE": 2000.0,
            "100K_COMBINE": 3000.0, 
            "150K_COMBINE": 4500.0,
            "FUNDED": 2000.0,  # Conservative funded limit
            "PRIVATE": 10000.0  # Higher limit for private
        }
        return limits.get(self.account_type, 2000.0)
    
    def get_progress_percent(self) -> float:
        """Get progress towards profit target"""
        if self.profit_target == 0:
            return 0.0
        return min(100.0, (self.total_pnl / self.profit_target) * 100)
    
    def get_daily_loss_percent(self) -> float:
        """Get percentage of daily loss limit used"""
        if self.daily_loss_limit == 0:
            return 0.0
        return min(100.0, (abs(min(0, self.daily_pnl)) / self.daily_loss_limit) * 100)
    
    def get_risk_score(self) -> int:
        """Get risk score 0-100"""
        factors = []
        
        # Daily loss factor
        daily_loss_pct = self.get_daily_loss_percent()
        factors.append(daily_loss_pct * 0.4)
        
        # Position count factor  
        position_count = len(self.positions)
        max_positions = 5
        factors.append((position_count / max_positions) * 25)
        
        # Drawdown factor
        drawdown_pct = (self.max_drawdown / self.account_size) * 100
        factors.append(min(drawdown_pct * 2, 35))
        
        return min(100, sum(factors))


class PortfolioManager:
    """Multi-account portfolio management system"""
    
    def __init__(self):
        self.accounts: Dict[str, Account] = {}
        self.copy_trading_enabled = False
        self.master_account_id = None
        self.total_capital_deployed = 0.0
        self.total_profits_withdrawn = 0.0
        self.private_account_balance = 0.0
        
        # Initialize session state
        self._initialize_portfolio_state()
    
    def _initialize_portfolio_state(self):
        """Initialize portfolio session state"""
        if 'portfolio_accounts' not in st.session_state:
            st.session_state.portfolio_accounts = {}
        if 'copy_trading_settings' not in st.session_state:
            st.session_state.copy_trading_settings = {
                'enabled': False,
                'master_account': None,
                'slave_accounts': [],
                'position_scaling': 1.0,
                'max_accounts': 5
            }
        if 'withdrawal_history' not in st.session_state:
            st.session_state.withdrawal_history = []
        if 'private_account_target' not in st.session_state:
            st.session_state.private_account_target = 100000.0  # $100K target
    
    def add_account(self, account_type: str, account_size: float, nickname: str = None) -> str:
        """Add new account to portfolio"""
        account_id = f"{account_type}_{uuid.uuid4().hex[:8]}"
        
        account = Account(account_id, account_type, account_size)
        if nickname:
            account.nickname = nickname
        
        self.accounts[account_id] = account
        st.session_state.portfolio_accounts[account_id] = account.__dict__
        
        return account_id
    
    def get_portfolio_summary(self) -> Dict[str, Any]:
        """Get comprehensive portfolio summary"""
        if not self.accounts:
            return {
                "total_accounts": 0,
                "total_capital": 0.0,
                "total_pnl": 0.0,
                "total_positions": 0,
                "active_accounts": 0,
                "funded_accounts": 0
            }
        
        total_capital = sum(acc.account_size for acc in self.accounts.values())
        total_pnl = sum(acc.total_pnl for acc in self.accounts.values())
        total_positions = sum(len(acc.positions) for acc in self.accounts.values())
        active_accounts = len([acc for acc in self.accounts.values() if acc.status == "Active"])
        funded_accounts = len([acc for acc in self.accounts.values() if acc.status == "Funded"])
        
        return {
            "total_accounts": len(self.accounts),
            "total_capital": total_capital,
            "total_pnl": total_pnl,
            "total_positions": total_positions,
            "active_accounts": active_accounts,
            "funded_accounts": funded_accounts,
            "daily_pnl": sum(acc.daily_pnl for acc in self.accounts.values()),
            "avg_risk_score": sum(acc.get_risk_score() for acc in self.accounts.values()) / len(self.accounts) if self.accounts else 0,
            "withdrawal_ready": self._get_withdrawal_ready_amount()
        }
    
    def _get_withdrawal_ready_amount(self) -> float:
        """Calculate amount ready for withdrawal to private account"""
        withdrawal_ready = 0.0
        for account in self.accounts.values():
            if account.status == "Funded" and account.total_pnl > 0:
                # Assuming 80% of profits can be withdrawn monthly
                withdrawal_ready += account.total_pnl * 0.8
        return withdrawal_ready
    
    def render_portfolio_dashboard(self):
        """Render main portfolio management dashboard"""
        st.markdown("# 📊 Multi-Account Portfolio Manager")
        st.markdown("### Scaling to 5x150K TopStep Accounts → Private Trading")
        
        # Portfolio Overview
        self._render_portfolio_overview()
        
        # Account Management
        self._render_account_management()
        
        # Copy Trading Controls
        self._render_copy_trading_controls()
        
        # Scaling Progress
        self._render_scaling_progress()
        
        # Withdrawal Management
        self._render_withdrawal_management()
    
    def _render_portfolio_overview(self):
        """Render portfolio overview section"""
        st.markdown("---")
        st.markdown("### 🎯 Portfolio Overview")
        
        summary = self.get_portfolio_summary()
        
        # Key metrics row
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.metric("Total Accounts", summary['total_accounts'], help="All accounts in portfolio")
            
        with col2:
            st.metric("Active Accounts", summary['active_accounts'], help="Currently trading accounts")
            
        with col3:
            st.metric("Total Capital", f"${summary['total_capital']:,.0f}", help="Combined account sizes")
            
        with col4:
            st.metric("Total Positions", summary['total_positions'], help="Open positions across all accounts")
            
        with col5:
            st.metric("Portfolio P&L", f"${summary['total_pnl']:+,.0f}", 
                     delta=f"${summary['daily_pnl']:+,.0f} today")
        
        # Portfolio composition chart
        if self.accounts:
            self._render_portfolio_composition_chart()
    
    def _render_portfolio_composition_chart(self):
        """Render portfolio composition visualization"""
        # Account status distribution
        status_counts = {}
        account_sizes = {}
        
        for account in self.accounts.values():
            status_counts[account.status] = status_counts.get(account.status, 0) + 1
            account_sizes[account.account_type] = account_sizes.get(account.account_type, 0) + account.account_size
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig_status = px.pie(
                values=list(status_counts.values()),
                names=list(status_counts.keys()),
                title="Account Status Distribution",
                color_discrete_map={
                    "Active": "#10b981",
                    "Funded": "#3b82f6", 
                    "Inactive": "#6b7280",
                    "Failed": "#ef4444"
                }
            )
            st.plotly_chart(fig_status, use_container_width=True)
        
        with col2:
            fig_size = px.bar(
                x=list(account_sizes.keys()),
                y=list(account_sizes.values()),
                title="Capital by Account Type",
                color=list(account_sizes.values()),
                color_continuous_scale="viridis"
            )
            fig_size.update_layout(showlegend=False)
            st.plotly_chart(fig_size, use_container_width=True)
    
    def _render_account_management(self):
        """Render account management section"""
        st.markdown("---")
        st.markdown("### 🏦 Account Management")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Accounts table
            if self.accounts:
                accounts_data = []
                for account in self.accounts.values():
                    accounts_data.append({
                        "Account ID": account.account_id[-8:],  # Last 8 chars
                        "Type": account.account_type,
                        "Size": f"${account.account_size:,.0f}",
                        "Status": account.status,
                        "Progress": f"{account.get_progress_percent():.1f}%",
                        "Daily P&L": f"${account.daily_pnl:+.0f}",
                        "Total P&L": f"${account.total_pnl:+.0f}",
                        "Positions": len(account.positions),
                        "Risk Score": f"{account.get_risk_score():.0f}/100"
                    })
                
                df = pd.DataFrame(accounts_data)
                st.dataframe(df, use_container_width=True, hide_index=True)
            else:
                st.info("No accounts added yet. Add your first account to get started.")
        
        with col2:
            # Add new account
            st.markdown("#### Add New Account")
            
            account_type = st.selectbox(
                "Account Type",
                ["50K_COMBINE", "100K_COMBINE", "150K_COMBINE", "FUNDED", "PRIVATE"]
            )
            
            account_sizes = {
                "50K_COMBINE": 50000,
                "100K_COMBINE": 100000,
                "150K_COMBINE": 150000,
                "FUNDED": 150000,
                "PRIVATE": 250000
            }
            
            account_size = st.number_input(
                "Account Size",
                value=account_sizes[account_type],
                step=1000,
                format="%d"
            )
            
            nickname = st.text_input("Nickname (optional)")
            
            if st.button("Add Account", type="primary", use_container_width=True):
                account_id = self.add_account(account_type, account_size, nickname)
                st.success(f"Added account {account_id[-8:]}")
                st.rerun()
    
    def _render_copy_trading_controls(self):
        """Render copy trading configuration"""
        st.markdown("---")
        st.markdown("### 🔄 Copy Trading System")
        st.markdown("**Goal**: Copy trades across 5x150K TopStep accounts for maximum scale")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            # Copy trading settings
            copy_enabled = st.checkbox(
                "Enable Copy Trading",
                value=st.session_state.copy_trading_settings['enabled'],
                help="Copy trades from master account to all slave accounts"
            )
            st.session_state.copy_trading_settings['enabled'] = copy_enabled
            
            if copy_enabled and self.accounts:
                master_account = st.selectbox(
                    "Master Account (Signal Source)",
                    options=list(self.accounts.keys()),
                    format_func=lambda x: f"{self.accounts[x].account_type} ({x[-8:]})",
                    help="This account will generate signals for all others"
                )
                st.session_state.copy_trading_settings['master_account'] = master_account
                
                # Position scaling
                position_scaling = st.slider(
                    "Position Size Scaling",
                    min_value=0.1,
                    max_value=2.0,
                    value=1.0,
                    step=0.1,
                    help="Scale position sizes on slave accounts"
                )
                st.session_state.copy_trading_settings['position_scaling'] = position_scaling
        
        with col2:
            # Copy trading status
            if copy_enabled:
                st.success("🟢 Copy Trading ACTIVE")
                
                if st.session_state.copy_trading_settings.get('master_account'):
                    master = self.accounts[st.session_state.copy_trading_settings['master_account']]
                    st.info(f"📡 Master: {master.account_type} ({master.account_id[-8:]})")
                    
                    slave_count = len(self.accounts) - 1
                    st.info(f"📱 Slaves: {slave_count} accounts")
                    
                    if slave_count > 0:
                        total_capital = sum(acc.account_size for acc in self.accounts.values() if acc.account_id != master.account_id)
                        st.metric("Total Slave Capital", f"${total_capital:,.0f}")
                        
                        potential_monthly = total_capital * 0.06  # 6% monthly target
                        st.metric("Potential Monthly Profit", f"${potential_monthly:,.0f}")
            else:
                st.warning("🔴 Copy Trading DISABLED")
                st.caption("Enable to scale across multiple accounts")
    
    def _render_scaling_progress(self):
        """Render scaling progress visualization"""
        st.markdown("---")
        st.markdown("### 📈 Scaling Progress to 5x150K Target")
        
        # Target configuration
        target_accounts = 5
        target_size = 150000
        total_target_capital = target_accounts * target_size
        
        current_capital = sum(acc.account_size for acc in self.accounts.values())
        current_150k_accounts = len([acc for acc in self.accounts.values() if acc.account_size == 150000])
        
        # Progress metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "150K Accounts",
                f"{current_150k_accounts}/5",
                help="Progress towards 5x150K account goal"
            )
        
        with col2:
            capital_progress = (current_capital / total_target_capital) * 100
            st.metric(
                "Capital Progress", 
                f"{capital_progress:.1f}%",
                help=f"${current_capital:,.0f} / ${total_target_capital:,.0f}"
            )
        
        with col3:
            funded_accounts = len([acc for acc in self.accounts.values() if acc.status == "Funded"])
            st.metric("Funded Accounts", funded_accounts, help="Accounts ready for withdrawal")
        
        with col4:
            withdrawal_ready = self._get_withdrawal_ready_amount()
            st.metric("Withdrawal Ready", f"${withdrawal_ready:,.0f}", help="Profits available for withdrawal")
        
        # Progress visualization
        progress_data = {
            "Target": [5, total_target_capital, 45000],  # 5 accounts, $750K total, $45K monthly profit target
            "Current": [len(self.accounts), current_capital, current_capital * 0.06]  # Current metrics
        }
        
        categories = ["Accounts", "Capital ($)", "Monthly Profit Potential ($)"]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(name="Target", x=categories, y=progress_data["Target"], marker_color="#ef4444"))
        fig.add_trace(go.Bar(name="Current", x=categories, y=progress_data["Current"], marker_color="#10b981"))
        
        fig.update_layout(
            title="Scaling Progress Overview",
            barmode='group',
            yaxis_title="Value"
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    def _render_withdrawal_management(self):
        """Render withdrawal tracking and management"""
        st.markdown("---")
        st.markdown("### 💰 Withdrawal Management → Private Account")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Withdrawal projections
            funded_accounts = [acc for acc in self.accounts.values() if acc.status == "Funded"]
            
            if funded_accounts:
                st.markdown("#### Monthly Withdrawal Projections")
                
                projections_data = []
                total_monthly_withdrawal = 0
                
                for account in funded_accounts:
                    monthly_profit = account.account_size * 0.06  # 6% monthly target
                    monthly_withdrawal = monthly_profit * 0.8     # 80% withdrawal rate
                    total_monthly_withdrawal += monthly_withdrawal
                    
                    projections_data.append({
                        "Account": account.account_id[-8:],
                        "Type": account.account_type,
                        "Monthly Profit Target": f"${monthly_profit:,.0f}",
                        "Withdrawable (80%)": f"${monthly_withdrawal:,.0f}",
                        "Status": account.status
                    })
                
                df_projections = pd.DataFrame(projections_data)
                st.dataframe(df_projections, use_container_width=True, hide_index=True)
                
                st.metric(
                    "Total Monthly Withdrawal Potential",
                    f"${total_monthly_withdrawal:,.0f}",
                    help="Total monthly withdrawals from all funded accounts"
                )
                
                # Timeline to private account goal
                private_target = st.session_state.private_account_target
                months_to_target = private_target / total_monthly_withdrawal if total_monthly_withdrawal > 0 else 0
                st.metric(
                    "Months to Private Account Goal",
                    f"{months_to_target:.1f}",
                    help=f"Time to reach ${private_target:,.0f} private account goal"
                )
            else:
                st.info("No funded accounts yet. Focus on passing combines to enable withdrawals.")
        
        with col2:
            # Withdrawal history and controls
            st.markdown("#### Withdrawal Controls")
            
            if st.button("Simulate Monthly Withdrawal", help="Simulate monthly profit withdrawal"):
                if funded_accounts:
                    total_withdrawal = sum(acc.account_size * 0.06 * 0.8 for acc in funded_accounts)
                    
                    withdrawal_record = {
                        "date": datetime.now().isoformat(),
                        "amount": total_withdrawal,
                        "accounts": len(funded_accounts),
                        "type": "monthly_withdrawal"
                    }
                    
                    st.session_state.withdrawal_history.append(withdrawal_record)
                    st.session_state.private_account_target -= total_withdrawal
                    
                    st.success(f"Simulated withdrawal: ${total_withdrawal:,.0f}")
                    st.rerun()
                else:
                    st.error("No funded accounts available for withdrawal")
            
            # Private account target
            new_target = st.number_input(
                "Private Account Target",
                value=st.session_state.private_account_target,
                step=10000,
                format="%d",
                help="Target amount for private trading account"
            )
            
            if new_target != st.session_state.private_account_target:
                st.session_state.private_account_target = new_target
                st.rerun()
            
            # Withdrawal history
            if st.session_state.withdrawal_history:
                st.markdown("#### Recent Withdrawals")
                for withdrawal in st.session_state.withdrawal_history[-5:]:
                    date = datetime.fromisoformat(withdrawal["date"]).strftime("%m/%d")
                    st.caption(f"{date}: ${withdrawal['amount']:,.0f}")
    
    def get_position_summary(self) -> Dict[str, Any]:
        """Get comprehensive position summary across all accounts"""
        total_positions = 0
        total_unrealized_pnl = 0.0
        position_breakdown = {"NQ": 0, "ES": 0, "CL": 0, "GC": 0}
        account_exposure = {}
        
        for account in self.accounts.values():
            account_positions = len(account.positions)
            total_positions += account_positions
            
            account_exposure[account.account_id[-8:]] = {
                "positions": account_positions,
                "unrealized_pnl": sum(pos.get("unrealized_pnl", 0) for pos in account.positions),
                "instruments": {}
            }
            
            for position in account.positions:
                symbol = position.get("symbol", "UNKNOWN")
                quantity = abs(position.get("quantity", 0))
                unrealized = position.get("unrealized_pnl", 0)
                
                position_breakdown[symbol] = position_breakdown.get(symbol, 0) + quantity
                total_unrealized_pnl += unrealized
                
                if symbol not in account_exposure[account.account_id[-8:]]["instruments"]:
                    account_exposure[account.account_id[-8:]]["instruments"][symbol] = 0
                account_exposure[account.account_id[-8:]]["instruments"][symbol] += quantity
        
        return {
            "total_positions": total_positions,
            "total_unrealized_pnl": total_unrealized_pnl,
            "position_breakdown": position_breakdown,
            "account_exposure": account_exposure,
            "max_risk_account": max(account_exposure.keys(), 
                                   key=lambda k: account_exposure[k]["positions"]) if account_exposure else None
        }


# Global portfolio manager instance
portfolio_manager = PortfolioManager()


def render_portfolio_page():
    """Render the portfolio management page"""
    portfolio_manager.render_portfolio_dashboard()


def get_portfolio_status():
    """Get current portfolio status for display in other pages"""
    summary = portfolio_manager.get_portfolio_summary()
    position_summary = portfolio_manager.get_position_summary()
    
    return {
        "accounts": summary["total_accounts"],
        "active_accounts": summary["active_accounts"], 
        "total_positions": position_summary["total_positions"],
        "total_capital": summary["total_capital"],
        "portfolio_pnl": summary["total_pnl"],
        "copy_trading": st.session_state.copy_trading_settings["enabled"]
    }


# Export key functions
__all__ = [
    'PortfolioManager',
    'portfolio_manager', 
    'render_portfolio_page',
    'get_portfolio_status'
]