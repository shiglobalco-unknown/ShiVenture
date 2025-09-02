#!/usr/bin/env python3
"""
Emergency Controls for Futures Portfolio Monitor
Kill switch and trading lock functionality for the web dashboard
"""

import streamlit as st
import asyncio
import os
import sys
import json
import logging
from datetime import datetime
from typing import Dict, Any, List
import subprocess


class EmergencyControlSystem:
    """Emergency control system for the trading dashboard"""
    
    def __init__(self):
        self.logger = self._setup_logging()
        self.emergency_log_file = f"emergency_actions_{datetime.now().strftime('%Y%m%d')}.log"
        
        # Initialize safety system attributes
        self.safety_rules = {}
        self.active_alerts = []
        self.alert_history = []
        
        # Initialize session state for emergency controls
        self._initialize_emergency_state()
        
    def _setup_logging(self):
        """Setup emergency logging"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        return logging.getLogger("EmergencyControls")
    
    def _initialize_emergency_state(self):
        """Initialize emergency control session state"""
        if 'emergency_stop_active' not in st.session_state:
            st.session_state.emergency_stop_active = False
        if 'trading_locked' not in st.session_state:
            st.session_state.trading_locked = False
        if 'kill_switch_armed' not in st.session_state:
            st.session_state.kill_switch_armed = False
        if 'emergency_actions' not in st.session_state:
            st.session_state.emergency_actions = []
        if 'last_emergency_check' not in st.session_state:
            st.session_state.last_emergency_check = datetime.now()

    def render_emergency_controls(self):
        """Render emergency controls panel in the dashboard"""
        st.markdown("---")
        st.markdown("### 🚨 Emergency Controls")
        
        # Create columns for emergency controls
        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
        
        with col1:
            self._render_kill_switch()
            
        with col2:
            self._render_trading_lock()
            
        with col3:
            self._render_position_closer()
            
        with col4:
            self._render_system_status()

    def _render_kill_switch(self):
        """Render kill switch control"""
        st.markdown("#### 💀 Kill Switch")
        
        # Arm/Disarm toggle
        armed = st.checkbox(
            "Arm Kill Switch", 
            value=st.session_state.kill_switch_armed,
            help="Arm the kill switch for immediate emergency stop",
            key="arm_kill_switch"
        )
        st.session_state.kill_switch_armed = armed
        
        # Kill switch button (only active when armed)
        if st.session_state.kill_switch_armed:
            if st.button(
                "🚨 EMERGENCY STOP", 
                type="primary",
                help="STOP ALL TRADING IMMEDIATELY",
                key="kill_switch_button",
                use_container_width=True
            ):
                self._execute_kill_switch()
        else:
            st.button(
                "🔒 Kill Switch (DISARMED)", 
                disabled=True,
                help="Arm the kill switch first",
                key="kill_switch_disabled",
                use_container_width=True
            )

    def _render_trading_lock(self):
        """Render trading lock toggle"""
        st.markdown("#### 🔐 Trading Lock")
        
        # Trading lock toggle
        locked = st.toggle(
            "Lock Trading",
            value=st.session_state.trading_locked,
            help="Prevent new trades while keeping existing positions",
            key="trading_lock_toggle"
        )
        
        if locked != st.session_state.trading_locked:
            st.session_state.trading_locked = locked
            self._log_emergency_action(
                "TRADING_LOCK", 
                f"Trading {'LOCKED' if locked else 'UNLOCKED'}",
                {"locked": locked}
            )
        
        # Status indicator
        if st.session_state.trading_locked:
            st.error("🔒 Trading is LOCKED")
            st.caption("No new positions can be opened")
        else:
            st.success("🟢 Trading is ACTIVE")
            st.caption("New positions can be opened")

    def _render_position_closer(self):
        """Render position closing controls"""
        st.markdown("#### 🏃‍♂️ Close Positions")
        
        if st.session_state.positions:
            # Close all positions button
            if st.button(
                f"Close All ({len(st.session_state.positions)})",
                type="secondary",
                help="Close all open positions immediately",
                key="close_all_positions",
                use_container_width=True
            ):
                self._close_all_positions()
            
            # Individual position controls
            st.caption(f"{len(st.session_state.positions)} open positions")
            
            # Show position summary
            for i, pos in enumerate(st.session_state.positions):
                col_a, col_b = st.columns([3, 1])
                with col_a:
                    pnl_color = "🟢" if pos["unrealized_pnl"] >= 0 else "🔴"
                    st.caption(f"{pnl_color} {pos['symbol']} {pos['side']} • ${pos['unrealized_pnl']:+.0f}")
                with col_b:
                    if st.button("❌", key=f"close_pos_{i}", help=f"Close {pos['symbol']} position"):
                        self._close_individual_position(i)
        else:
            st.info("No open positions")

    def _render_system_status(self):
        """Render system status indicators"""
        st.markdown("#### ⚡ System Status")
        
        # Emergency status
        if st.session_state.emergency_stop_active:
            st.error("🚨 EMERGENCY STOP ACTIVE")
        elif st.session_state.trading_locked:
            st.warning("🔒 Trading Locked")
        else:
            st.success("🟢 System Active")
        
        # System health indicators
        health_indicators = self._get_system_health()
        
        for indicator, status in health_indicators.items():
            if status:
                st.success(f"✅ {indicator}")
            else:
                st.error(f"❌ {indicator}")

    def _execute_kill_switch(self):
        """Execute emergency kill switch"""
        try:
            st.session_state.emergency_stop_active = True
            
            # Log emergency action
            self._log_emergency_action(
                "KILL_SWITCH",
                "Emergency kill switch activated",
                {"positions_closed": len(st.session_state.positions)}
            )
            
            # Close all positions immediately
            if st.session_state.positions:
                total_pnl = 0
                for pos in st.session_state.positions:
                    total_pnl += pos["unrealized_pnl"]
                
                st.session_state.daily_pnl += total_pnl
                st.session_state.total_pnl += total_pnl
                st.session_state.positions.clear()
            
            # Stop automated trading engines
            self._stop_trading_engines()
            
            # Lock trading
            st.session_state.trading_locked = True
            
            # Show emergency alert
            st.error("🚨 EMERGENCY STOP EXECUTED - ALL POSITIONS CLOSED")
            st.error("🔒 Trading is now LOCKED until manual override")
            
            # Create emergency report
            self._create_emergency_report()
            
        except Exception as e:
            st.error(f"❌ Error executing kill switch: {e}")
            self.logger.error(f"Kill switch execution error: {e}")

    def _close_all_positions(self):
        """Close all open positions"""
        try:
            if not st.session_state.positions:
                st.warning("No positions to close")
                return
            
            total_pnl = 0
            position_count = len(st.session_state.positions)
            
            # Calculate total P&L
            for pos in st.session_state.positions:
                total_pnl += pos["unrealized_pnl"]
            
            # Close all positions
            st.session_state.positions.clear()
            
            # Update P&L
            st.session_state.daily_pnl += total_pnl
            st.session_state.total_pnl += total_pnl
            
            # Log action
            self._log_emergency_action(
                "CLOSE_ALL_POSITIONS",
                f"Closed {position_count} positions",
                {"position_count": position_count, "total_pnl": total_pnl}
            )
            
            # Show confirmation
            pnl_color = "success" if total_pnl >= 0 else "error"
            st.success(f"✅ Closed {position_count} positions • P&L: ${total_pnl:+.2f}")
            
        except Exception as e:
            st.error(f"❌ Error closing positions: {e}")
            self.logger.error(f"Position closing error: {e}")

    def _close_individual_position(self, position_index: int):
        """Close individual position"""
        try:
            if position_index >= len(st.session_state.positions):
                st.error("Invalid position index")
                return
            
            pos = st.session_state.positions[position_index]
            pnl = pos["unrealized_pnl"]
            
            # Remove position
            st.session_state.positions.pop(position_index)
            
            # Update P&L
            st.session_state.daily_pnl += pnl
            st.session_state.total_pnl += pnl
            
            # Log action
            self._log_emergency_action(
                "CLOSE_POSITION",
                f"Closed {pos['symbol']} position",
                {"symbol": pos['symbol'], "side": pos['side'], "pnl": pnl}
            )
            
            # Show confirmation
            st.success(f"✅ Closed {pos['symbol']} {pos['side']} • P&L: ${pnl:+.2f}")
            
        except Exception as e:
            st.error(f"❌ Error closing position: {e}")
            self.logger.error(f"Individual position closing error: {e}")

    def _stop_trading_engines(self):
        """Stop automated trading engines"""
        try:
            # Try to stop the automated trading engine
            trading_processes = [
                "automated_trading_engine.py",
                "main.py",
                "deploy.py"
            ]
            
            stopped_processes = []
            for process in trading_processes:
                try:
                    result = subprocess.run(
                        ["pkill", "-f", process], 
                        capture_output=True, 
                        text=True
                    )
                    if result.returncode == 0:
                        stopped_processes.append(process)
                except:
                    pass
            
            # Try to activate external kill switch
            try:
                safety_script = os.path.join(
                    os.path.dirname(os.path.dirname(__file__)),
                    "Futures-Trading-Automation",
                    "safety_controls.py"
                )
                if os.path.exists(safety_script):
                    subprocess.run([sys.executable, safety_script, "kill"], timeout=10)
            except:
                pass
                
            if stopped_processes:
                st.info(f"🛑 Stopped processes: {', '.join(stopped_processes)}")
            
        except Exception as e:
            self.logger.error(f"Error stopping trading engines: {e}")

    def _get_system_health(self) -> Dict[str, bool]:
        """Get system health indicators"""
        health = {
            "Dashboard": True,  # If we're here, dashboard is working
            "Session State": bool(st.session_state),
            "Emergency Logs": os.path.exists(self.emergency_log_file)
        }
        
        # Check for trading engine processes
        try:
            result = subprocess.run(
                ["pgrep", "-f", "automated_trading"], 
                capture_output=True, 
                text=True
            )
            health["Trading Engine"] = bool(result.stdout.strip())
        except:
            health["Trading Engine"] = False
            
        return health

    def _log_emergency_action(self, action_type: str, description: str, data: Dict[str, Any] = None):
        """Log emergency action"""
        try:
            action = {
                "timestamp": datetime.now().isoformat(),
                "action_type": action_type,
                "description": description,
                "data": data or {},
                "user_session": st.session_state.get("session_id", "unknown")
            }
            
            # Add to session state
            st.session_state.emergency_actions.append(action)
            
            # Keep only last 50 actions
            if len(st.session_state.emergency_actions) > 50:
                st.session_state.emergency_actions = st.session_state.emergency_actions[-50:]
            
            # Log to file
            with open(self.emergency_log_file, "a") as f:
                f.write(json.dumps(action) + "\n")
            
            # Log to system
            self.logger.info(f"Emergency action: {action_type} - {description}")
            
        except Exception as e:
            self.logger.error(f"Error logging emergency action: {e}")

    def _create_emergency_report(self):
        """Create emergency situation report"""
        try:
            report = {
                "timestamp": datetime.now().isoformat(),
                "emergency_type": "KILL_SWITCH_ACTIVATION",
                "system_state": {
                    "positions_at_emergency": len(st.session_state.get("positions", [])),
                    "daily_pnl": st.session_state.get("daily_pnl", 0),
                    "total_pnl": st.session_state.get("total_pnl", 0),
                    "trading_locked": st.session_state.get("trading_locked", False),
                    "emergency_stop_active": st.session_state.get("emergency_stop_active", False)
                },
                "recent_actions": st.session_state.get("emergency_actions", [])[-10:],
                "system_health": self._get_system_health()
            }
            
            report_filename = f"emergency_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(report_filename, "w") as f:
                json.dump(report, f, indent=2)
            
            st.info(f"📄 Emergency report saved: {report_filename}")
            
        except Exception as e:
            st.error(f"❌ Error creating emergency report: {e}")

    def render_emergency_status_bar(self):
        """Render emergency status bar at top of dashboard"""
        if st.session_state.emergency_stop_active:
            st.error("🚨 **EMERGENCY STOP ACTIVE** - All trading stopped. Manual intervention required.")
        elif st.session_state.trading_locked:
            st.warning("🔒 **Trading Locked** - New positions prevented. Existing positions active.")
        elif st.session_state.kill_switch_armed:
            st.warning("⚠️ **Kill Switch Armed** - Emergency stop ready for activation.")

    def render_recent_emergency_actions(self):
        """Render recent emergency actions log"""
        if st.session_state.emergency_actions:
            st.markdown("#### 📋 Recent Emergency Actions")
            
            # Show last 10 actions
            recent_actions = st.session_state.emergency_actions[-10:]
            
            for action in reversed(recent_actions):
                action_time = datetime.fromisoformat(action["timestamp"]).strftime("%H:%M:%S")
                
                if action["action_type"] == "KILL_SWITCH":
                    st.error(f"🚨 {action_time} - {action['description']}")
                elif action["action_type"] == "TRADING_LOCK":
                    st.warning(f"🔒 {action_time} - {action['description']}")
                elif action["action_type"] in ["CLOSE_ALL_POSITIONS", "CLOSE_POSITION"]:
                    st.info(f"❌ {action_time} - {action['description']}")
                else:
                    st.caption(f"ℹ️ {action_time} - {action['description']}")

    def reset_emergency_state(self):
        """Reset emergency state (admin function)"""
        if st.button("🔄 Reset Emergency State", help="Admin function to reset emergency state"):
            st.session_state.emergency_stop_active = False
            st.session_state.trading_locked = False
            st.session_state.kill_switch_armed = False
            st.success("✅ Emergency state reset")
            self._log_emergency_action("RESET_EMERGENCY", "Emergency state manually reset")


# Singleton instance
emergency_controls = EmergencyControlSystem()


def add_emergency_controls_to_page():
    """Add emergency controls to current page"""
    emergency_controls.render_emergency_status_bar()
    emergency_controls.render_emergency_controls()


def add_emergency_sidebar():
    """Add emergency controls to sidebar"""
    with st.sidebar:
        st.markdown("### 🚨 Emergency")
        
        # Quick status
        if st.session_state.get("emergency_stop_active"):
            st.error("EMERGENCY STOP")
        elif st.session_state.get("trading_locked"):
            st.warning("Trading Locked")
        else:
            st.success("System Active")
        
        # Quick controls
        if st.button("🔒 Toggle Trading Lock", key="sidebar_trading_lock", use_container_width=True):
            st.session_state.trading_locked = not st.session_state.get("trading_locked", False)
            st.rerun()
        
        if st.session_state.get("positions"):
            if st.button("❌ Close All Positions", key="sidebar_close_all", use_container_width=True):
                emergency_controls._close_all_positions()
                st.rerun()


# Export functions for use in main app
__all__ = [
    'emergency_controls',
    'add_emergency_controls_to_page',
    'add_emergency_sidebar',
    'EmergencyControlSystem'
]