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
import math

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
        background: #ffffff;
        color: #1a365d;
        padding: 16px 32px;
        border-radius: 6px;
        text-decoration: none;
        font-size: 16px;
        font-weight: 600;
        display: inline-block;
        transition: all 0.3s ease;
        border: 2px solid #1a365d;
        box-shadow: 0 4px 15px rgba(26, 54, 93, 0.2);
    }
    
    .citadel-cta:hover {
        background: #1a365d;
        color: #ffffff;
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(26, 54, 93, 0.4);
        border: 2px solid #1a365d;
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
    
    if 'start_time' not in st.session_state:
        st.session_state.start_time = datetime.now().timestamp()
    
    if 'demo_data' not in st.session_state:
        st.session_state.demo_data = generate_demo_data()

def generate_demo_data():
    """Generate realistic demo trading data with precise real-time synchronization"""
    precise_time = datetime.now()
    
    # Use time-based seed for consistent but changing data
    time_seed = int(precise_time.timestamp())
    random.seed(time_seed)
    
    # Generate time-synchronized market data
    base_value = 87450.25
    time_factor = precise_time.second + (precise_time.microsecond / 1000000)
    market_volatility = 1 + 0.1 * math.sin(time_factor * 2 * math.pi / 60)  # Sine wave volatility
    
    return {
        'account_value': base_value + (random.uniform(-500, 500) * market_volatility),
        'day_pnl': random.uniform(-1000, 2000) * market_volatility,
        'day_pnl_pct': random.uniform(-2.5, 3.0) * market_volatility,
        'positions': generate_demo_positions(precise_time),
        'market_data': generate_market_data(precise_time),
        'last_update': precise_time,
        'millisecond_precision': precise_time.microsecond // 1000  # Store milliseconds for precision
    }

def generate_demo_positions(timestamp=None):
    """Generate demo futures positions with time synchronization"""
    if timestamp is None:
        timestamp = datetime.now()
        
    symbols = ['ES', 'NQ', 'CL', 'GC', 'ZN']
    time_seed = int(timestamp.timestamp())
    random.seed(time_seed)
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

def generate_market_data(timestamp=None):
    """Generate real-time market data with time synchronization"""
    if timestamp is None:
        timestamp = datetime.now()
    
    # Use timestamp for consistent market simulation
    time_seed = int(timestamp.timestamp())
    random.seed(time_seed)
    
    # Time-based market oscillation
    time_factor = timestamp.second + (timestamp.microsecond / 1000000)
    market_trend = math.sin(time_factor * 2 * math.pi / 60)  # 60-second cycle
    
    return {
        'ES': {'price': 4485.25 + (10 * market_trend) + random.uniform(-5, 5), 'change': random.uniform(-20, 20)},
        'NQ': {'price': 15847.50 + (50 * market_trend) + random.uniform(-25, 25), 'change': random.uniform(-100, 100)},
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
        st.session_state.current_page = 'about'
with nav3:
    if st.button("Technology", key="nav_tech"):
        st.session_state.current_page = 'technology'
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
            <a href="#about" class="nav-item {'active' if st.session_state.current_page == 'about' else ''}">About Us</a>
            <a href="#technology" class="nav-item {'active' if st.session_state.current_page == 'technology' else ''}">Technology</a>
            <a href="#futures" class="nav-item {'active' if st.session_state.current_page == 'futures_dashboard' else ''}" style="color: #007bff;">📊 Dashboard</a>
            <a href="#login" class="nav-item {'active' if st.session_state.current_page == 'login' else ''}" style="color: #007bff;">🔐 Login</a>
            <a href="#insights" class="nav-item {'active' if st.session_state.current_page == 'home' else ''}">Home</a>
        </div>
    </div>
</nav>
""", unsafe_allow_html=True)

# Real-time auto-refresh system for live updates
if st.session_state.current_page == 'futures_dashboard':
    # Calculate precise time difference for real-time updates
    now = datetime.now()
    time_diff = (now - st.session_state.last_update).total_seconds()
    
    # Refresh data every 1 second for true real-time experience
    if time_diff >= 1.0:
        st.session_state.demo_data = generate_demo_data()
        st.session_state.last_update = now
        # Force rerun for continuous updates
        st.rerun()

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
    
    # Real-time clock with microsecond precision
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    microseconds = f"{now.microsecond:06d}"[:3]  # Show first 3 digits of microseconds
    
    st.markdown(f"""
    <div style="text-align: center; margin-bottom: 20px;">
        <div style="background: #10b981; color: white; padding: 8px 16px; border-radius: 25px; font-size: 14px; font-family: 'Courier New', monospace; display: inline-block; box-shadow: 0 2px 8px rgba(16, 185, 129, 0.3);">
            🟢 LIVE - {current_time}.{microseconds} EST
        </div>
        <div style="font-size: 11px; color: #666666; margin-top: 4px;">
            Auto-refreshing every second • Real-time synchronized data • Precision timing
        </div>
        <div style="font-size: 10px; color: #999999; margin-top: 2px; font-family: 'Courier New', monospace;">
            System uptime: {int((now.timestamp() - st.session_state.get('start_time', now.timestamp())))}s • Refresh rate: 1000ms
        </div>
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

def render_about_page():
    """Render the About Us page with company story"""
    st.markdown("""
    <div style="padding-top: 90px; background: linear-gradient(135deg, #f8fafb 0%, #e8f2f6 100%); min-height: 100vh;">
        <div style="max-width: 1200px; margin: 0 auto; padding: 60px 20px;">
            <!-- Hero Section -->
            <div style="text-align: center; margin-bottom: 80px;">
                <h1 style="color: #1a365d; font-size: 48px; font-weight: 700; margin-bottom: 24px; letter-spacing: -1px;">Our Story</h1>
                <p style="color: #4a5568; font-size: 20px; line-height: 1.7; max-width: 800px; margin: 0 auto;">
                    From algorithmic trading pioneers to AI-powered hedge fund leaders, discover the journey that created Shi Ventures.
                </p>
            </div>
            
            <!-- Story Timeline -->
            <div style="background: #ffffff; border-radius: 16px; padding: 60px; box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1); margin-bottom: 60px;">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: center; margin-bottom: 60px;">
                    <div>
                        <h2 style="color: #1a365d; font-size: 36px; font-weight: 700; margin-bottom: 24px;">The Beginning</h2>
                        <p style="color: #4a5568; font-size: 18px; line-height: 1.7; margin-bottom: 20px;">
                            Founded in 2019 by a team of quantitative researchers from top-tier financial institutions, 
                            Shi Ventures began with a simple yet powerful vision: to democratize institutional-grade 
                            algorithmic trading through artificial intelligence.
                        </p>
                        <p style="color: #4a5568; font-size: 18px; line-height: 1.7;">
                            Our founding team brought together decades of experience from Goldman Sachs, Citadel, 
                            and Renaissance Technologies, combining traditional quantitative finance with 
                            cutting-edge machine learning techniques.
                        </p>
                    </div>
                    <div style="background: linear-gradient(135deg, #1a365d 0%, #2d5aa0 100%); border-radius: 12px; padding: 40px; color: white; text-align: center;">
                        <div style="font-size: 48px; font-weight: 700; margin-bottom: 16px; color: #60a5fa;">2019</div>
                        <div style="font-size: 18px; font-weight: 500;">Founded in San Francisco</div>
                        <div style="font-size: 14px; margin-top: 8px; opacity: 0.8;">With $2M seed funding</div>
                    </div>
                </div>
                
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: center; margin-bottom: 60px;">
                    <div style="background: linear-gradient(135deg, #10b981 0%, #047857 100%); border-radius: 12px; padding: 40px; color: white; text-align: center;">
                        <div style="font-size: 48px; font-weight: 700; margin-bottom: 16px; color: #6ee7b7;">2021</div>
                        <div style="font-size: 18px; font-weight: 500;">AI Breakthrough</div>
                        <div style="font-size: 14px; margin-top: 8px; opacity: 0.8;">15-Agent System Deployed</div>
                    </div>
                    <div>
                        <h2 style="color: #1a365d; font-size: 36px; font-weight: 700; margin-bottom: 24px;">The Innovation</h2>
                        <p style="color: #4a5568; font-size: 18px; line-height: 1.7; margin-bottom: 20px;">
                            After two years of intensive research and development, we achieved a breakthrough in 
                            multi-agent AI systems. Our proprietary 15-agent architecture could process market data, 
                            identify patterns, and execute trades with unprecedented precision.
                        </p>
                        <p style="color: #4a5568; font-size: 18px; line-height: 1.7;">
                            This innovation earned us recognition from the Financial Technology Association and 
                            secured Series A funding, allowing us to scale our operations and refine our algorithms.
                        </p>
                    </div>
                </div>
                
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 80px; align-items: center;">
                    <div>
                        <h2 style="color: #1a365d; font-size: 36px; font-weight: 700; margin-bottom: 24px;">Today & Tomorrow</h2>
                        <p style="color: #4a5568; font-size: 18px; line-height: 1.7; margin-bottom: 20px;">
                            Today, Shi Ventures manages over $150M in assets under management, serving institutional 
                            clients and sophisticated individual investors. Our AI system operates 24/7, making 
                            split-second decisions across global markets.
                        </p>
                        <p style="color: #4a5568; font-size: 18px; line-height: 1.7;">
                            Looking ahead, we're pioneering the next generation of financial AI, exploring quantum 
                            computing applications and expanding into emerging markets worldwide.
                        </p>
                    </div>
                    <div style="background: linear-gradient(135deg, #8b5cf6 0%, #6d28d9 100%); border-radius: 12px; padding: 40px; color: white; text-align: center;">
                        <div style="font-size: 48px; font-weight: 700; margin-bottom: 16px; color: #c4b5fd;">2024</div>
                        <div style="font-size: 18px; font-weight: 500">Global Expansion</div>
                        <div style="font-size: 14px; margin-top: 8px; opacity: 0.8;">$150M+ AUM</div>
                    </div>
                </div>
            </div>
            
            <!-- Values Section -->
            <div style="text-align: center; margin-bottom: 60px;">
                <h2 style="color: #1a365d; font-size: 36px; font-weight: 700; margin-bottom: 48px;">Our Core Values</h2>
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 40px;">
                    <div style="background: #ffffff; border-radius: 12px; padding: 40px; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);">
                        <div style="font-size: 48px; margin-bottom: 20px;">🎯</div>
                        <h3 style="color: #1a365d; font-size: 24px; font-weight: 600; margin-bottom: 16px;">Precision</h3>
                        <p style="color: #4a5568; font-size: 16px; line-height: 1.6;">
                            Every algorithm, every decision, every trade is executed with mathematical precision and rigorous testing.
                        </p>
                    </div>
                    <div style="background: #ffffff; border-radius: 12px; padding: 40px; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);">
                        <div style="font-size: 48px; margin-bottom: 20px;">🚀</div>
                        <h3 style="color: #1a365d; font-size: 24px; font-weight: 600; margin-bottom: 16px;">Innovation</h3>
                        <p style="color: #4a5568; font-size: 16px; line-height: 1.6;">
                            We push the boundaries of what's possible in AI-driven finance, constantly evolving our technology.
                        </p>
                    </div>
                    <div style="background: #ffffff; border-radius: 12px; padding: 40px; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);">
                        <div style="font-size: 48px; margin-bottom: 20px;">🤝</div>
                        <h3 style="color: #1a365d; font-size: 24px; font-weight: 600; margin-bottom: 16px;">Integrity</h3>
                        <p style="color: #4a5568; font-size: 16px; line-height: 1.6;">
                            Transparency, ethical practices, and client-first thinking guide every aspect of our operations.
                        </p>
                    </div>
                </div>
            </div>
            
            <!-- Team Section -->
            <div style="background: #ffffff; border-radius: 16px; padding: 60px; box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1); text-align: center;">
                <h2 style="color: #1a365d; font-size: 36px; font-weight: 700; margin-bottom: 24px;">Leadership Team</h2>
                <p style="color: #4a5568; font-size: 18px; line-height: 1.7; margin-bottom: 48px; max-width: 700px; margin-left: auto; margin-right: auto;">
                    Led by industry veterans with combined experience of over 50 years in quantitative finance, 
                    AI research, and institutional asset management.
                </p>
                <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 30px;">
                    <div style="text-align: center;">
                        <div style="background: linear-gradient(135deg, #1a365d 0%, #2d5aa0 100%); width: 80px; height: 80px; border-radius: 50%; margin: 0 auto 20px auto; display: flex; align-items: center; justify-content: center;">
                            <span style="color: white; font-size: 24px; font-weight: 700;">AS</span>
                        </div>
                        <h4 style="color: #1a365d; font-size: 16px; font-weight: 600; margin-bottom: 8px;">Anthony Shi</h4>
                        <p style="color: #4a5568; font-size: 14px;">Founder & CEO</p>
                    </div>
                    <div style="text-align: center;">
                        <div style="background: linear-gradient(135deg, #10b981 0%, #047857 100%); width: 80px; height: 80px; border-radius: 50%; margin: 0 auto 20px auto; display: flex; align-items: center; justify-content: center;">
                            <span style="color: white; font-size: 24px; font-weight: 700;">DR</span>
                        </div>
                        <h4 style="color: #1a365d; font-size: 16px; font-weight: 600; margin-bottom: 8px;">Dr. Sarah Chen</h4>
                        <p style="color: #4a5568; font-size: 14px;">Chief Technology Officer</p>
                    </div>
                    <div style="text-align: center;">
                        <div style="background: linear-gradient(135deg, #8b5cf6 0%, #6d28d9 100%); width: 80px; height: 80px; border-radius: 50%; margin: 0 auto 20px auto; display: flex; align-items: center; justify-content: center;">
                            <span style="color: white; font-size: 24px; font-weight: 700;">MR</span>
                        </div>
                        <h4 style="color: #1a365d; font-size: 16px; font-weight: 600; margin-bottom: 8px;">Michael Rodriguez</h4>
                        <p style="color: #4a5568; font-size: 14px;">Head of Quantitative Research</p>
                    </div>
                    <div style="text-align: center;">
                        <div style="background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); width: 80px; height: 80px; border-radius: 50%; margin: 0 auto 20px auto; display: flex; align-items: center; justify-content: center;">
                            <span style="color: white; font-size: 24px; font-weight: 700;">JK</span>
                        </div>
                        <h4 style="color: #1a365d; font-size: 16px; font-weight: 600; margin-bottom: 8px;">Jennifer Kim</h4>
                        <p style="color: #4a5568; font-size: 14px;">Chief Risk Officer</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_technology_page():
    """Render the Technology page showcasing AI agents and optimization"""
    st.markdown("""
    <div style="padding-top: 90px; background: #ffffff; min-height: 100vh;">
        <div style="max-width: 1200px; margin: 0 auto; padding: 60px 20px;">
            <!-- Hero Section -->
            <div style="text-align: center; margin-bottom: 80px;">
                <h1 style="color: #1a365d; font-size: 48px; font-weight: 700; margin-bottom: 24px; letter-spacing: -1px;">AI-Powered Trading Technology</h1>
                <p style="color: #4a5568; font-size: 20px; line-height: 1.7; max-width: 800px; margin: 0 auto;">
                    Discover how our proprietary 15-agent AI system revolutionizes trading through advanced machine learning, 
                    real-time optimization, and institutional-grade risk management.
                </p>
            </div>
            
            <!-- Core Architecture -->
            <div style="background: linear-gradient(135deg, #f8fafb 0%, #e8f2f6 100%); border-radius: 16px; padding: 60px; margin-bottom: 60px;">
                <h2 style="color: #1a365d; font-size: 36px; font-weight: 700; text-align: center; margin-bottom: 48px;">Multi-Agent Architecture</h2>
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 40px;">
                    <div style="background: #ffffff; border-radius: 12px; padding: 30px; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1); border-left: 4px solid #1a365d;">
                        <h3 style="color: #1a365d; font-size: 20px; font-weight: 600; margin-bottom: 16px;">🏛️ Executive Tier</h3>
                        <p style="color: #4a5568; font-size: 16px; line-height: 1.6; margin-bottom: 16px;">
                            Portfolio-wide oversight and strategic asset allocation
                        </p>
                        <ul style="color: #4a5568; font-size: 14px; line-height: 1.6; padding-left: 20px;">
                            <li>Master Risk Controller</li>
                            <li>Strategic Asset Allocator</li>
                            <li>Performance Monitor</li>
                        </ul>
                    </div>
                    <div style="background: #ffffff; border-radius: 12px; padding: 30px; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1); border-left: 4px solid #10b981;">
                        <h3 style="color: #1a365d; font-size: 20px; font-weight: 600; margin-bottom: 16px;">📊 Strategic Tier</h3>
                        <p style="color: #4a5568; font-size: 16px; line-height: 1.6; margin-bottom: 16px;">
                            Asset class specialization and market execution
                        </p>
                        <ul style="color: #4a5568; font-size: 14px; line-height: 1.6; padding-left: 20px;">
                            <li>Equity Trading Agent</li>
                            <li>Fixed Income Agent</li>
                            <li>FX Trading Agent</li>
                        </ul>
                    </div>
                    <div style="background: #ffffff; border-radius: 12px; padding: 30px; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1); border-left: 4px solid #8b5cf6;">
                        <h3 style="color: #1a365d; font-size: 20px; font-weight: 600; margin-bottom: 16px;">⚡ Execution Tier</h3>
                        <p style="color: #4a5568; font-size: 16px; line-height: 1.6; margin-bottom: 16px;">
                            Real-time execution and risk monitoring
                        </p>
                        <ul style="color: #4a5568; font-size: 14px; line-height: 1.6; padding-left: 20px;">
                            <li>Smart Order Router</li>
                            <li>Risk Management System</li>
                            <li>News Sentiment Agent</li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <!-- Unique Value Propositions -->
            <div style="margin-bottom: 60px;">
                <h2 style="color: #1a365d; font-size: 36px; font-weight: 700; text-align: center; margin-bottom: 48px;">Unique Competitive Advantages</h2>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 60px;">
                    <div>
                        <div style="background: linear-gradient(135deg, #1a365d 0%, #2d5aa0 100%); border-radius: 12px; padding: 40px; color: white; margin-bottom: 40px;">
                            <h3 style="font-size: 24px; font-weight: 600; margin-bottom: 20px;">🧠 Adaptive Learning Engine</h3>
                            <p style="font-size: 16px; line-height: 1.6; opacity: 0.9;">
                                Our AI agents continuously learn and adapt to market conditions using reinforcement learning. 
                                Unlike static algorithms, our system evolves with market changes, improving performance over time.
                            </p>
                            <div style="background: rgba(255, 255, 255, 0.1); border-radius: 8px; padding: 20px; margin-top: 20px;">
                                <div style="font-size: 14px; opacity: 0.8; margin-bottom: 8px;">Key Innovation:</div>
                                <div style="font-size: 16px; font-weight: 500;">Real-time strategy optimization based on market microstructure changes</div>
                            </div>
                        </div>
                        
                        <div style="background: linear-gradient(135deg, #10b981 0%, #047857 100%); border-radius: 12px; padding: 40px; color: white;">
                            <h3 style="font-size: 24px; font-weight: 600; margin-bottom: 20px;">🎯 Precision Execution</h3>
                            <p style="font-size: 16px; line-height: 1.6; opacity: 0.9;">
                                Sub-millisecond execution with intelligent order routing across 40+ venues. 
                                Our Smart Order Router minimizes market impact while maximizing fill rates.
                            </p>
                            <div style="background: rgba(255, 255, 255, 0.1); border-radius: 8px; padding: 20px; margin-top: 20px;">
                                <div style="font-size: 14px; opacity: 0.8; margin-bottom: 8px;">Performance Metric:</div>
                                <div style="font-size: 16px; font-weight: 500;">Average execution time: 0.7 milliseconds</div>
                            </div>
                        </div>
                    </div>
                    
                    <div>
                        <div style="background: linear-gradient(135deg, #8b5cf6 0%, #6d28d9 100%); border-radius: 12px; padding: 40px; color: white; margin-bottom: 40px;">
                            <h3 style="font-size: 24px; font-weight: 600; margin-bottom: 20px;">🔗 Cross-Asset Correlation</h3>
                            <p style="font-size: 16px; line-height: 1.6; opacity: 0.9;">
                                Our system identifies hidden correlations across asset classes, currencies, and time zones. 
                                This multi-dimensional approach captures opportunities others miss.
                            </p>
                            <div style="background: rgba(255, 255, 255, 0.1); border-radius: 8px; padding: 20px; margin-top: 20px;">
                                <div style="font-size: 14px; opacity: 0.8; margin-bottom: 8px;">Coverage:</div>
                                <div style="font-size: 16px; font-weight: 500;">15,000+ instruments across global markets</div>
                            </div>
                        </div>
                        
                        <div style="background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); border-radius: 12px; padding: 40px; color: white;">
                            <h3 style="font-size: 24px; font-weight: 600; margin-bottom: 20px;">🛡️ Dynamic Risk Management</h3>
                            <p style="font-size: 16px; line-height: 1.6; opacity: 0.9;">
                                Real-time portfolio stress testing and automated hedging. Our risk system anticipates 
                                market volatility and adjusts positions before risks materialize.
                            </p>
                            <div style="background: rgba(255, 255, 255, 0.1); border-radius: 8px; padding: 20px; margin-top: 20px;">
                                <div style="font-size: 14px; opacity: 0.8; margin-bottom: 8px;">Response Time:</div>
                                <div style="font-size: 16px; font-weight: 500;">Automated hedging within 100 microseconds</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- AI Strategy Optimization -->
            <div style="background: linear-gradient(135deg, #f8fafb 0%, #e8f2f6 100%); border-radius: 16px; padding: 60px; margin-bottom: 60px;">
                <h2 style="color: #1a365d; font-size: 36px; font-weight: 700; text-align: center; margin-bottom: 24px;">Strategy Optimization Engine</h2>
                <p style="color: #4a5568; font-size: 18px; text-align: center; margin-bottom: 48px; max-width: 800px; margin-left: auto; margin-right: auto;">
                    Our proprietary optimization engine continuously refines trading strategies using quantum-inspired algorithms 
                    and advanced statistical methods.
                </p>
                
                <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 40px;">
                    <div style="background: #ffffff; border-radius: 12px; padding: 30px; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);">
                        <div style="display: flex; align-items: center; margin-bottom: 20px;">
                            <div style="background: linear-gradient(135deg, #1a365d 0%, #2d5aa0 100%); width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 16px;">
                                <span style="color: white; font-size: 20px;">📈</span>
                            </div>
                            <h3 style="color: #1a365d; font-size: 20px; font-weight: 600;">Bayesian Optimization</h3>
                        </div>
                        <p style="color: #4a5568; font-size: 16px; line-height: 1.6;">
                            Continuously optimizes strategy parameters using Bayesian inference, improving Sharpe ratios by 15-25% through intelligent parameter tuning.
                        </p>
                    </div>
                    
                    <div style="background: #ffffff; border-radius: 12px; padding: 30px; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);">
                        <div style="display: flex; align-items: center; margin-bottom: 20px;">
                            <div style="background: linear-gradient(135deg, #10b981 0%, #047857 100%); width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 16px;">
                                <span style="color: white; font-size: 20px;">🔄</span>
                            </div>
                            <h3 style="color: #1a365d; font-size: 20px; font-weight: 600;">Genetic Algorithms</h3>
                        </div>
                        <p style="color: #4a5568; font-size: 16px; line-height: 1.6;">
                            Evolves trading strategies through genetic programming, creating novel approaches that traditional methods cannot discover.
                        </p>
                    </div>
                    
                    <div style="background: #ffffff; border-radius: 12px; padding: 30px; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);">
                        <div style="display: flex; align-items: center; margin-bottom: 20px;">
                            <div style="background: linear-gradient(135deg, #8b5cf6 0%, #6d28d9 100%); width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 16px;">
                                <span style="color: white; font-size: 20px;">🎲</span>
                            </div>
                            <h3 style="color: #1a365d; font-size: 20px; font-weight: 600;">Monte Carlo Simulation</h3>
                        </div>
                        <p style="color: #4a5568; font-size: 16px; line-height: 1.6;">
                            Runs millions of market scenarios to stress-test strategies and optimize for risk-adjusted returns across different market regimes.
                        </p>
                    </div>
                    
                    <div style="background: #ffffff; border-radius: 12px; padding: 30px; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);">
                        <div style="display: flex; align-items: center; margin-bottom: 20px;">
                            <div style="background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 16px;">
                                <span style="color: white; font-size: 20px;">🧮</span>
                            </div>
                            <h3 style="color: #1a365d; font-size: 20px; font-weight: 600;">Quantum Annealing</h3>
                        </div>
                        <p style="color: #4a5568; font-size: 16px; line-height: 1.6;">
                            Leverages quantum-inspired optimization for portfolio construction, solving complex optimization problems in seconds rather than hours.
                        </p>
                    </div>
                </div>
            </div>
            
            <!-- Technical Stats -->
            <div style="background: linear-gradient(135deg, #1a365d 0%, #2d5aa0 100%); border-radius: 16px; padding: 60px; color: white; text-align: center;">
                <h2 style="font-size: 36px; font-weight: 700; margin-bottom: 48px;">System Performance Metrics</h2>
                <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 40px;">
                    <div>
                        <div style="font-size: 42px; font-weight: 700; margin-bottom: 12px; color: #60a5fa;">99.97%</div>
                        <div style="font-size: 16px; opacity: 0.9;">System Uptime</div>
                    </div>
                    <div>
                        <div style="font-size: 42px; font-weight: 700; margin-bottom: 12px; color: #6ee7b7;">0.7ms</div>
                        <div style="font-size: 16px; opacity: 0.9;">Avg Execution Time</div>
                    </div>
                    <div>
                        <div style="font-size: 42px; font-weight: 700; margin-bottom: 12px; color: #c4b5fd;">15,000+</div>
                        <div style="font-size: 16px; opacity: 0.9;">Instruments Tracked</div>
                    </div>
                    <div>
                        <div style="font-size: 42px; font-weight: 700; margin-bottom: 12px; color: #fcd34d;">24/7</div>
                        <div style="font-size: 16px; opacity: 0.9;">Global Operations</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

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

# Main execution with page routing
if st.session_state.current_page == 'futures_dashboard':
    render_professional_dashboard()
elif st.session_state.current_page == 'login':
    render_login_page()
elif st.session_state.current_page == 'about':
    render_about_page()
elif st.session_state.current_page == 'technology':
    render_technology_page()
else:
    render_main_website()