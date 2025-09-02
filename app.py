"""
Shi Ventures - Enhanced AI Hedge Fund Platform
Professional trading interface with real-time updates and live dashboard
Domain: shiventure.com - Sanitized for public GitHub repository
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import sys
import os
from datetime import datetime, timedelta
import time
import random

# Add components directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'components'))

# Page config
st.set_page_config(
    page_title="Shi Ventures - Where Global Markets Evolve",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Enhanced Citadel-style CSS (same as original)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body, .stApp {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        background-color: #ffffff;
        color: #32373c;
        line-height: 1.6;
    }
    
    /* Remove Streamlit branding completely */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp > header {visibility: hidden;}
    .stDeployButton {visibility: hidden;}
    .stActionButton {visibility: hidden;}
    div[data-testid="stToolbar"] {visibility: hidden;}
    div[data-testid="stDecoration"] {visibility: hidden;}
    div[data-testid="stStatusWidget"] {visibility: hidden;}
    .stApp > div:first-child {margin-top: 0;}
    
    /* Citadel Navigation */
    .citadel-nav {
        background: #ffffff;
        border-bottom: 1px solid #e6e6e6;
        padding: 0;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        height: 70px;
    }
    
    .nav-container {
        max-width: 1200px;
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
        height: 70px;
        padding: 0 20px;
    }
    
    .citadel-logo {
        font-size: 24px;
        font-weight: 700;
        color: #32373c;
        text-decoration: none;
        letter-spacing: -0.5px;
    }
    
    .nav-menu {
        display: flex;
        align-items: center;
        gap: 40px;
    }
    
    .nav-item {
        color: #32373c;
        text-decoration: none;
        font-size: 16px;
        font-weight: 400;
        transition: color 0.2s ease;
        cursor: pointer;
    }
    
    .nav-item:hover {
        color: #000000;
    }
    
    .nav-item.active {
        color: #007bff;
        font-weight: 500;
    }
    
    /* Hero Section */
    .hero-section {
        position: relative;
        background: #ffffff;
        padding-top: 70px;
        min-height: 100vh;
        display: flex;
        align-items: center;
        overflow: hidden;
    }
    
    .hero-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 60px 20px;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 80px;
        align-items: center;
        position: relative;
        z-index: 3;
    }
    
    .hero-content h1 {
        font-size: 48px;
        font-weight: 700;
        color: #32373c;
        line-height: 1.2;
        margin-bottom: 24px;
        letter-spacing: -1px;
    }
    
    .hero-content p {
        font-size: 20px;
        color: #666666;
        line-height: 1.6;
        margin-bottom: 40px;
        font-weight: 400;
    }
    
    .citadel-cta {
        background: #007bff;
        color: #ffffff;
        padding: 16px 32px;
        border-radius: 4px;
        text-decoration: none;
        font-size: 16px;
        font-weight: 500;
        display: inline-block;
        transition: all 0.3s ease;
    }
    
    .citadel-cta:hover {
        background: #0056b3;
        color: #ffffff;
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 123, 255, 0.3);
    }
    
    /* Stats Section */
    .stats-section {
        background: #ffffff;
        padding: 100px 20px;
        border-top: 1px solid #e6e6e6;
        border-bottom: 1px solid #e6e6e6;
    }
    
    .stats-container {
        max-width: 1200px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 60px;
    }
    
    .large-stat {
        text-align: center;
        padding: 40px 20px;
    }
    
    .large-stat-number {
        font-size: 72px;
        font-weight: 700;
        color: #007bff;
        margin-bottom: 16px;
        line-height: 1;
    }
    
    .large-stat-prefix {
        font-size: 48px;
        vertical-align: top;
    }
    
    .large-stat-suffix {
        font-size: 48px;
    }
    
    .large-stat-label {
        font-size: 16px;
        color: #32373c;
        font-weight: 400;
        line-height: 1.4;
        max-width: 280px;
        margin: 0 auto;
    }
    
    /* Content Sections */
    .content-section {
        padding: 100px 20px;
        background: #ffffff;
    }
    
    .section-container {
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .section-split {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 80px;
        align-items: center;
    }
    
    .content-left h2 {
        font-size: 42px;
        font-weight: 700;
        color: #32373c;
        line-height: 1.2;
        margin-bottom: 32px;
        letter-spacing: -1px;
    }
    
    .content-right p {
        font-size: 18px;
        color: #666666;
        line-height: 1.7;
        margin-bottom: 24px;
    }
    
    /* Footer */
    .citadel-footer {
        background: #32373c;
        color: #ffffff;
        padding: 80px 20px 40px 20px;
    }
    
    .footer-container {
        max-width: 1200px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 60px;
        margin-bottom: 40px;
    }
    
    .footer-logo {
        font-size: 24px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 20px;
    }
    
    .footer-nav {
        display: flex;
        gap: 40px;
        justify-content: flex-end;
        flex-wrap: wrap;
    }
    
    .footer-nav a {
        color: #ffffff;
        text-decoration: none;
        font-size: 16px;
        font-weight: 400;
        transition: color 0.2s;
    }
    
    .footer-nav a:hover {
        color: #cccccc;
    }
    
    .footer-bottom {
        border-top: 1px solid #555555;
        padding-top: 30px;
        text-align: center;
        color: #cccccc;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
def initialize_session_state():
    """Initialize session state with real-time data"""
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'home'
    
    if 'user_authenticated' not in st.session_state:
        st.session_state.user_authenticated = False
    
    if 'last_update' not in st.session_state:
        st.session_state.last_update = datetime.now()
    
    if 'demo_data' not in st.session_state:
        st.session_state.demo_data = generate_demo_data()

def generate_demo_data():
    """Generate realistic demo trading data with live updates"""
    base_time = datetime.now()
    
    return {
        'account_value': 87450.25 + random.uniform(-500, 500),
        'day_pnl': random.uniform(-1000, 2000),
        'day_pnl_pct': random.uniform(-2.5, 3.0),
        'positions': generate_demo_positions(),
        'market_data': generate_market_data(),
        'last_update': base_time
    }

def generate_demo_positions():
    """Generate demo futures positions"""
    symbols = ['ES', 'NQ', 'CL', 'GC', 'ZN']
    positions = []
    
    for symbol in random.sample(symbols, 3):  # Random 3 positions
        qty = random.choice([-3, -2, -1, 1, 2, 3])
        entry_price = random.uniform(3000, 5000)
        current_price = entry_price * (1 + random.uniform(-0.02, 0.03))
        
        positions.append({
            'symbol': symbol,
            'description': get_symbol_description(symbol),
            'quantity': qty,
            'entry_price': entry_price,
            'current_price': current_price,
            'unrealized_pnl': qty * (current_price - entry_price) * 50,  # Demo multiplier
        })
    
    return positions

def get_symbol_description(symbol):
    """Get futures contract descriptions"""
    descriptions = {
        'ES': 'E-mini S&P 500',
        'NQ': 'E-mini NASDAQ-100',
        'CL': 'Crude Oil',
        'GC': 'Gold',
        'ZN': '10-Year Treasury Note'
    }
    return descriptions.get(symbol, symbol)

def generate_market_data():
    """Generate live market data simulation"""
    return {
        'ES': {'price': 4485.25 + random.uniform(-10, 10), 'change': random.uniform(-20, 20)},
        'NQ': {'price': 15847.50 + random.uniform(-50, 50), 'change': random.uniform(-100, 100)},
        'CL': {'price': 82.45 + random.uniform(-2, 2), 'change': random.uniform(-3, 3)},
        'GC': {'price': 2045.20 + random.uniform(-10, 10), 'change': random.uniform(-15, 15)},
    }

# Initialize session state
initialize_session_state()

# Navigation buttons (hidden)
nav1, nav2, nav3, nav4, nav5 = st.columns(5)
with nav1:
    if st.button("Home", key="nav_home"):
        st.session_state.current_page = 'home'
with nav2:
    if st.button("About", key="nav_about"):
        st.session_state.current_page = 'home'
with nav3:
    if st.button("Technology", key="nav_tech"):
        st.session_state.current_page = 'home'
with nav4:
    if st.button("Futures Dashboard", key="nav_futures"):
        st.session_state.current_page = 'futures_dashboard'
with nav5:
    if st.button("Login", key="nav_login"):
        st.session_state.current_page = 'login'

# Visual Navigation Bar
st.markdown(f"""
<nav class="citadel-nav">
    <div class="nav-container">
        <a href="#" class="citadel-logo">SHI VENTURES</a>
        <div class="nav-menu">
            <a href="#about" class="nav-item {'active' if st.session_state.current_page == 'home' else ''}">Who We Are</a>
            <a href="#technology" class="nav-item {'active' if st.session_state.current_page == 'home' else ''}">What We Do</a>
            <a href="#futures" class="nav-item {'active' if st.session_state.current_page == 'futures_dashboard' else ''}" style="color: #007bff;">📊 Dashboard</a>
            <a href="#login" class="nav-item {'active' if st.session_state.current_page == 'login' else ''}" style="color: #007bff;">🔐 Login</a>
            <a href="#insights" class="nav-item {'active' if st.session_state.current_page == 'home' else ''}">Insights</a>
        </div>
    </div>
</nav>
""", unsafe_allow_html=True)

# Auto-refresh every 5 seconds for live updates
if st.session_state.current_page == 'futures_dashboard':
    # Check if data needs refreshing (every 5 seconds)
    if (datetime.now() - st.session_state.last_update).seconds > 5:
        st.session_state.demo_data = generate_demo_data()
        st.session_state.last_update = datetime.now()

def render_professional_dashboard():
    """Professional trading dashboard with live updates"""
    
    st.markdown("""
    <div style="padding-top: 90px; background: #ffffff; min-height: 100vh;">
        <div style="max-width: 1400px; margin: 0 auto; padding: 40px 20px;">
            <div style="text-align: center; margin-bottom: 40px;">
                <h1 style="color: #32373c; font-size: 42px; font-weight: 700; margin-bottom: 16px;">Professional Trading Dashboard</h1>
                <p style="color: #666666; font-size: 18px; margin-bottom: 20px;">Real-time portfolio monitoring with live updates</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Live update indicator
    current_time = datetime.now().strftime("%H:%M:%S EST")
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 20px;">
        <span style="background: #10b981; color: white; padding: 4px 12px; border-radius: 20px; font-size: 12px;">
            🟢 LIVE - Last Updated: {current_time}
        </span>
    </div>
    """, unsafe_allow_html=True)
    
    # Account overview metrics
    demo_data = st.session_state.demo_data
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        pnl_delta = f"+${demo_data['day_pnl']:.2f}" if demo_data['day_pnl'] >= 0 else f"${demo_data['day_pnl']:.2f}"
        st.metric("Account Value", f"${demo_data['account_value']:,.2f}", 
                 f"{pnl_delta} ({demo_data['day_pnl_pct']:+.2f}%)")
    
    with col2:
        buying_power = demo_data['account_value'] * 0.5  # Demo calculation
        st.metric("Buying Power", f"${buying_power:,.2f}")
    
    with col3:
        total_pnl = sum(p['unrealized_pnl'] for p in demo_data['positions'])
        st.metric("Unrealized P&L", f"${total_pnl:+,.2f}")
    
    with col4:
        st.metric("Active Positions", len(demo_data['positions']), "Demo Account")
    
    # Main dashboard layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        render_positions_table()
        render_performance_chart()
    
    with col2:
        render_market_panel()
        render_demo_controls()

def render_positions_table():
    """Live updating positions table"""
    
    st.markdown("### Current Positions")
    
    positions = st.session_state.demo_data['positions']
    
    if positions:
        # Create DataFrame with formatted data
        df_data = []
        for pos in positions:
            df_data.append({
                'Symbol': pos['symbol'],
                'Description': pos['description'],
                'Quantity': f"{pos['quantity']:+d}",
                'Entry Price': f"${pos['entry_price']:,.2f}",
                'Current Price': f"${pos['current_price']:,.2f}",
                'Unrealized P&L': f"${pos['unrealized_pnl']:+,.2f}"
            })
        
        df = pd.DataFrame(df_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.info("No open positions")

def render_performance_chart():
    """Demo performance chart with live updates"""
    
    st.markdown("### Portfolio Performance")
    
    # Generate demo time series data
    dates = pd.date_range(start='2024-01-01', end=datetime.now(), freq='D')[-30:]
    base_value = st.session_state.demo_data['account_value']
    values = [base_value + random.uniform(-2000, 2000) for _ in range(len(dates))]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dates,
        y=values,
        mode='lines',
        line=dict(color='#10b981', width=2),
        name='Portfolio Value'
    ))
    
    fig.update_layout(
        height=300,
        margin=dict(l=0, r=0, t=20, b=0),
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        yaxis_title="Value ($)",
    )
    
    st.plotly_chart(fig, use_container_width=True)

def render_market_panel():
    """Live market data panel"""
    
    st.markdown("### Live Market Data")
    
    market_data = st.session_state.demo_data['market_data']
    
    for symbol, data in market_data.items():
        with st.container():
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"**{symbol}** - {get_symbol_description(symbol)}")
                
                change_color = "green" if data['change'] >= 0 else "red"
                change_sign = "+" if data['change'] >= 0 else ""
                
                st.markdown(f"""
                <div style="font-size: 18px; font-weight: 600;">${data['price']:,.2f}</div>
                <div style="color: {change_color}; font-size: 14px;">{change_sign}{data['change']:,.2f}</div>
                """, unsafe_allow_html=True)
            
            with col2:
                if st.button("📈", key=f"chart_{symbol}"):
                    st.info(f"Chart for {symbol} - Demo feature")

def render_demo_controls():
    """Demo emergency controls (sanitized)"""
    
    st.markdown("### Demo Controls")
    
    st.markdown("**🚨 Emergency Controls Preview**")
    st.info("Professional risk management interface available for authorized accounts.")
    
    if st.button("🔒 Demo Trading Lock", use_container_width=True):
        st.success("Demo: Trading would be locked to prevent new positions")
        time.sleep(1)
    
    if st.button("💀 Demo Emergency Stop", use_container_width=True):
        st.error("Demo: All positions would be closed immediately")
        time.sleep(1)
    
    st.markdown("**📊 Portfolio Actions**")
    if st.button("📈 New Position", use_container_width=True):
        st.info("Demo: Order entry interface would open")
    
    if st.button("🔄 Refresh Data", use_container_width=True):
        st.session_state.demo_data = generate_demo_data()
        st.session_state.last_update = datetime.now()
        st.rerun()

def render_login_page():
    """Professional login interface"""
    
    st.markdown("""
    <div style="padding-top: 90px; background: #ffffff; min-height: 100vh;">
        <div style="max-width: 600px; margin: 0 auto; padding: 40px 20px;">
            <div style="text-align: center; margin-bottom: 40px;">
                <h1 style="color: #32373c; font-size: 32px; font-weight: 700;">Secure Login</h1>
                <p style="color: #666666;">Access your professional trading account</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Account Access")
        username = st.text_input("Username", placeholder="Enter username")
        password = st.text_input("Password", type="password", placeholder="Enter password")
        
        if st.button("Demo Login", type="primary", use_container_width=True):
            st.session_state.user_authenticated = True
            st.session_state.current_page = 'futures_dashboard'
            st.success("Demo login successful!")
            time.sleep(1)
            st.rerun()
    
    with col2:
        st.markdown("### Security Features")
        st.markdown("""
        🔒 **256-bit SSL Encryption**  
        Bank-level security for all data
        
        🛡️ **Multi-Factor Authentication**  
        Additional security layer protection
        
        📱 **Device Recognition**  
        Trusted devices for seamless access
        
        🔔 **Login Alerts**  
        Instant notifications for account access
        """)

def render_main_website():
    """Render main AI hedge fund website"""
    
    # Display main AI hedge fund website
    st.markdown("""
    <section class="hero-section" style="background: linear-gradient(135deg, rgba(248, 250, 252, 0.95) 0%, rgba(226, 232, 240, 0.9) 100%), url('https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=1600&auto=format&fit=crop&q=80'); background-size: cover; background-position: center;">
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(135deg, rgba(255, 255, 255, 0.92) 0%, rgba(248, 250, 252, 0.88) 100%); z-index: 2;"></div>
        <div class="hero-container">
            <div class="hero-content">
                <h1 style="color: #1a365d;">Where Global Markets Evolve</h1>
                <p style="color: #4a5568;">Resilient and efficient markets drive economic opportunity. Through our AI trading, research and technology, we move markets forward.</p>
                <a href="#about" class="citadel-cta">Explore Who We Are</a>
            </div>
            <div style="background: linear-gradient(135deg, #1a365d 0%, #2d5aa0 100%); color: white; padding: 40px; border-radius: 8px; box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1); position: relative; z-index: 3;">
                <div style="position: relative; border-radius: 8px; overflow: hidden; margin-bottom: 30px;">
                    <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&auto=format&fit=crop&q=80" 
                         alt="AI Trading Technology" 
                         style="width: 100%; height: 300px; object-fit: cover; opacity: 0.7;">
                    <div style="position: absolute; top: 20px; left: 20px; background: rgba(255, 255, 255, 0.9); color: #1a365d; padding: 10px 16px; border-radius: 6px; font-size: 14px; font-weight: 600;">
                        🤖 AI SYSTEM ACTIVE
                    </div>
                    <div style="position: absolute; bottom: 20px; right: 20px; background: rgba(16, 185, 129, 0.9); color: white; padding: 6px 12px; border-radius: 4px; font-size: 12px; font-weight: 500;">
                        ● LIVE
                    </div>
                </div>
                <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px;">
                    <div style="text-align: center; padding: 20px; background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.2); border-radius: 6px;">
                        <div style="font-size: 32px; font-weight: 700; color: #60a5fa; margin-bottom: 8px;">15</div>
                        <div style="font-size: 12px; color: rgba(255, 255, 255, 0.8); text-transform: uppercase; letter-spacing: 0.5px;">AI Agents</div>
                    </div>
                    <div style="text-align: center; padding: 20px; background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.2); border-radius: 6px;">
                        <div style="font-size: 32px; font-weight: 700; color: #60a5fa; margin-bottom: 8px;">5</div>
                        <div style="font-size: 12px; color: rgba(255, 255, 255, 0.8); text-transform: uppercase; letter-spacing: 0.5px;">System Tiers</div>
                    </div>
                    <div style="text-align: center; padding: 20px; background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.2); border-radius: 6px;">
                        <div style="font-size: 32px; font-weight: 700; color: #60a5fa; margin-bottom: 8px;">24/7</div>
                        <div style="font-size: 12px; color: rgba(255, 255, 255, 0.8); text-transform: uppercase; letter-spacing: 0.5px;">Operations</div>
                    </div>
                    <div style="text-align: center; padding: 20px; background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.2); border-radius: 6px;">
                        <div style="font-size: 32px; font-weight: 700; color: #60a5fa; margin-bottom: 8px;">100%</div>
                        <div style="font-size: 12px; color: rgba(255, 255, 255, 0.8); text-transform: uppercase; letter-spacing: 0.5px;">Systematic</div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)

    # About Section
    st.markdown("""
    <section class="content-section" id="about">
        <div class="section-container">
            <div class="section-split">
                <div class="content-left">
                    <h2>The Next-Generation Capital Markets Firm</h2>
                </div>
                <div class="content-right">
                    <p>Our work is powered by the deepest integration of financial, mathematical and engineering expertise.</p>
                    <p>Combining deep trading acumen with cutting-edge analytics and technology, we deliver critical liquidity to the world's most important financial institutions—while helping shape the global markets of tomorrow.</p>
                    <a href="#technology" class="citadel-cta">Explore What We Do</a>
                </div>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)

    # Stats Section  
    st.markdown("""
    <section class="stats-section">
        <div class="stats-container">
            <div class="large-stat">
                <div class="large-stat-number">
                    <span class="large-stat-prefix">#</span>1
                </div>
                <div class="large-stat-label">In U.S. AI trading market making, with ~35% U.S.-listed retail volume executed through our platform</div>
            </div>
            <div class="large-stat">
                <div class="large-stat-number">
                    <span class="large-stat-prefix">$</span>66<span class="large-stat-suffix">B</span>
                </div>
                <div class="large-stat-label">in assets executed a day (approximate notional value in 24 hours, excluding swaps)</div>
            </div>
            <div class="large-stat">
                <div class="large-stat-number">
                    8<span class="large-stat-suffix">x</span>
                </div>
                <div class="large-stat-label">years as a Risk Awards Flow Market Maker of the Year, from 2017 to 2024</div>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)

# Footer (always shown)
st.markdown("""
<footer class="citadel-footer" id="contact">
    <div class="footer-container">
        <div class="footer-left">
            <div class="footer-logo">SHI VENTURES | AI Securities</div>
        </div>
        <div class="footer-right">
            <nav class="footer-nav">
                <a href="#about">Who We Are</a>
                <a href="#technology">What We Do</a>
                <a href="#insights">News & Insights</a>
                <a href="#careers">Careers</a>
            </nav>
        </div>
    </div>
    <div class="footer-bottom">
        <p>Copyright © Shi Ventures AI LLC or one of its affiliates. All rights reserved.</p>
        <p style="margin-top: 10px; font-size: 12px;">
            Investment advisory services provided by Shi Ventures AI LLC, a registered investment advisor. Past performance does not guarantee future results. All investments involve risk of loss.
        </p>
        <div style="text-align: center; padding-top: 20px; border-top: 1px solid #555555; margin-top: 20px;">
            <a href="#" style="color: #cccccc; font-size: 12px; text-decoration: underline;">View footnotes for this page.</a>
        </div>
    </div>
</footer>
""", unsafe_allow_html=True)

# Main execution
if st.session_state.current_page == 'futures_dashboard':
    render_professional_dashboard()
elif st.session_state.current_page == 'login':
    render_login_page()
else:
    render_main_website()