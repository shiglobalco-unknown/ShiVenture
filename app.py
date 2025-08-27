"""
Shi Ventures - Enhanced Institutional AI Hedge Fund Platform
Professional Citadel-inspired design with comprehensive content and media
Domain: shiventure.com
"""

import streamlit as st

# Page config
st.set_page_config(
    page_title="Shi Ventures - Where Global Markets Evolve",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Enhanced Citadel-style CSS with media support
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
    }
    
    .nav-item:hover {
        color: #000000;
    }
    
    /* Hero Section with Video Background */
    .hero-section {
        position: relative;
        background: #ffffff;
        padding-top: 70px;
        min-height: 100vh;
        display: flex;
        align-items: center;
        overflow: hidden;
    }
    
    .hero-video {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        opacity: 0.1;
        z-index: 1;
    }
    
    .hero-overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(248, 250, 252, 0.9) 100%);
        z-index: 2;
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
    
    .hero-visual {
        position: relative;
        background: #f8f9fa;
        border-radius: 8px;
        padding: 40px;
        text-align: center;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
    }
    
    .hero-image {
        width: 100%;
        height: 300px;
        object-fit: cover;
        border-radius: 8px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
    }
    
    .hero-stats {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 20px;
        margin-top: 30px;
    }
    
    .stat-item {
        text-align: center;
        padding: 20px;
        background: #ffffff;
        border-radius: 6px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    
    .stat-item:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
    }
    
    .stat-number {
        font-size: 32px;
        font-weight: 700;
        color: #32373c;
        margin-bottom: 8px;
    }
    
    .stat-label {
        font-size: 12px;
        color: #666666;
        font-weight: 400;
        text-transform: uppercase;
        letter-spacing: 0.5px;
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
    
    .section-image {
        width: 100%;
        height: 400px;
        object-fit: cover;
        border-radius: 12px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    
    .section-image:hover {
        transform: translateY(-5px);
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
    }
    
    /* Video Section */
    .video-section {
        background: #f8f9fa;
        padding: 100px 20px;
        text-align: center;
    }
    
    .video-container {
        max-width: 900px;
        margin: 0 auto;
    }
    
    .video-container h2 {
        font-size: 42px;
        font-weight: 700;
        color: #32373c;
        margin-bottom: 24px;
        letter-spacing: -1px;
    }
    
    .video-container p {
        font-size: 18px;
        color: #666666;
        margin-bottom: 40px;
    }
    
    .demo-video {
        width: 100%;
        height: 500px;
        border-radius: 12px;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
    }
    
    /* Stats Section - Large Numbers */
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
    
    /* AI System Grid */
    .ai-system-section {
        background: #f8f9fa;
        padding: 100px 20px;
    }
    
    .ai-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 30px;
        margin-top: 60px;
    }
    
    .ai-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 30px;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        border-left: 4px solid #007bff;
    }
    
    .ai-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
    }
    
    .ai-card h3 {
        font-size: 18px;
        font-weight: 600;
        color: #32373c;
        margin-bottom: 12px;
    }
    
    .ai-card p {
        font-size: 14px;
        color: #666666;
        line-height: 1.6;
    }
    
    .tier-badge {
        background: #007bff;
        color: #ffffff;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: 600;
        margin-bottom: 16px;
        display: inline-block;
    }
    
    /* Team Section */
    .team-section {
        background: #ffffff;
        padding: 100px 20px;
    }
    
    .team-stats {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 40px;
        margin-top: 60px;
    }
    
    .team-stat {
        text-align: center;
        padding: 40px 20px;
        background: #f8f9fa;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease;
    }
    
    .team-stat:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
    }
    
    .team-stat-number {
        font-size: 42px;
        font-weight: 700;
        color: #007bff;
        margin-bottom: 12px;
    }
    
    .team-stat-label {
        font-size: 14px;
        color: #666666;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Blue Section */
    .blue-section {
        background: linear-gradient(135deg, #007bff 0%, #0056b3 100%);
        color: #ffffff;
        padding: 100px 20px;
        position: relative;
        overflow: hidden;
    }
    
    .blue-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="dots" width="20" height="20" patternUnits="userSpaceOnUse"><circle cx="10" cy="10" r="1" fill="rgba(255,255,255,0.1)"/></pattern></defs><rect width="100" height="100" fill="url(%23dots)"/></svg>');
        opacity: 0.3;
    }
    
    .blue-section h2 {
        font-size: 42px;
        font-weight: 700;
        color: #ffffff;
        line-height: 1.2;
        margin-bottom: 32px;
        letter-spacing: -1px;
        position: relative;
        z-index: 2;
    }
    
    .blue-section p {
        font-size: 18px;
        color: rgba(255, 255, 255, 0.9);
        line-height: 1.7;
        position: relative;
        z-index: 2;
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
    
    /* Responsive Design */
    @media (max-width: 1024px) {
        .hero-container, .section-split {
            gap: 60px;
        }
        
        .stats-container {
            grid-template-columns: repeat(2, 1fr);
            gap: 40px;
        }
        
        .ai-grid {
            grid-template-columns: repeat(2, 1fr);
        }
        
        .team-stats {
            grid-template-columns: repeat(2, 1fr);
        }
    }
    
    @media (max-width: 768px) {
        .hero-container, .section-split, .stats-container, .footer-container {
            grid-template-columns: 1fr;
            gap: 40px;
        }
        
        .hero-content h1 {
            font-size: 36px;
        }
        
        .content-left h2, .blue-section h2, .video-container h2 {
            font-size: 32px;
        }
        
        .large-stat-number {
            font-size: 48px;
        }
        
        .nav-menu {
            display: none;
        }
        
        .ai-grid, .team-stats {
            grid-template-columns: 1fr;
        }
        
        .demo-video {
            height: 300px;
        }
    }
</style>
""", unsafe_allow_html=True)

# Navigation
st.markdown("""
<nav class="citadel-nav">
    <div class="nav-container">
        <a href="#" class="citadel-logo">SHI VENTURES</a>
        <div class="nav-menu">
            <a href="#about" class="nav-item">Who We Are</a>
            <a href="#technology" class="nav-item">What We Do</a>
            <a href="#insights" class="nav-item">News & Insights</a>
            <a href="#careers" class="nav-item">Careers</a>
            <span style="color: #32373c; font-size: 14px; cursor: pointer;">EN ▼</span>
        </div>
    </div>
</nav>
""", unsafe_allow_html=True)

# Hero Section with Professional Background
st.markdown("""
<section class="hero-section" style="background: linear-gradient(135deg, rgba(248, 250, 252, 0.95) 0%, rgba(226, 232, 240, 0.9) 100%), url('https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=1600&auto=format&fit=crop&q=80'); background-size: cover; background-position: center;">
    <div class="hero-overlay" style="background: linear-gradient(135deg, rgba(255, 255, 255, 0.92) 0%, rgba(248, 250, 252, 0.88) 100%);"></div>
    <div class="hero-container">
        <div class="hero-content">
            <h1 style="color: #1a365d;">Where Global Markets Evolve</h1>
            <p style="color: #4a5568;">Resilient and efficient markets drive economic opportunity. Through our AI trading, research and technology, we move markets forward.</p>
            <a href="#about" class="citadel-cta">Explore Who We Are</a>
        </div>
        <div class="hero-visual" style="background: linear-gradient(135deg, #1a365d 0%, #2d5aa0 100%); color: white; position: relative;">
            <div style="position: relative; border-radius: 8px; overflow: hidden;">
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
            <div class="hero-stats" style="margin-top: 30px;">
                <div class="stat-item" style="background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.2);">
                    <div class="stat-number" style="color: #60a5fa;">15</div>
                    <div class="stat-label" style="color: rgba(255, 255, 255, 0.8);">AI Agents</div>
                </div>
                <div class="stat-item" style="background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.2);">
                    <div class="stat-number" style="color: #60a5fa;">5</div>
                    <div class="stat-label" style="color: rgba(255, 255, 255, 0.8);">System Tiers</div>
                </div>
                <div class="stat-item" style="background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.2);">
                    <div class="stat-number" style="color: #60a5fa;">24/7</div>
                    <div class="stat-label" style="color: rgba(255, 255, 255, 0.8);">Operations</div>
                </div>
                <div class="stat-item" style="background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.2);">
                    <div class="stat-number" style="color: #60a5fa;">100%</div>
                    <div class="stat-label" style="color: rgba(255, 255, 255, 0.8);">Systematic</div>
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

# Video Demonstration Section with Professional GIF
st.markdown("""
<section class="video-section">
    <div class="video-container">
        <h2>See Our AI System in Action</h2>
        <p>Watch how our 15-agent system processes market data, makes trading decisions, and manages risk in real-time.</p>
        <div style="position: relative; background: linear-gradient(135deg, #1e3a5f 0%, #2d5aa0 100%); border-radius: 12px; padding: 40px; box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);">
            <img src="https://media.giphy.com/media/3oKIPEqDGUULpEU0aQ/giphy.gif" 
                 alt="AI Trading System Demo" 
                 style="width: 100%; height: 400px; object-fit: cover; border-radius: 8px; opacity: 0.9;">
            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center; color: white;">
                <div style="background: rgba(0, 0, 0, 0.7); padding: 20px; border-radius: 8px; backdrop-filter: blur(10px);">
                    <h3 style="margin: 0 0 10px 0; font-size: 24px; font-weight: 600;">Live AI Trading Dashboard</h3>
                    <p style="margin: 0; font-size: 14px; opacity: 0.9;">15 Agents • Real-time Processing • Risk Management</p>
                </div>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# AI System Architecture Section
st.markdown("""
<section class="ai-system-section" id="technology">
    <div class="section-container">
        <div style="text-align: center; margin-bottom: 60px;">
            <h2 style="font-size: 42px; font-weight: 700; color: #32373c; margin-bottom: 24px; letter-spacing: -1px;">15-Agent AI Trading System</h2>
            <p style="font-size: 18px; color: #666666; max-width: 800px; margin: 0 auto;">Our proprietary multi-agent system operates across five hierarchical tiers, each specialized for different aspects of trading and risk management.</p>
        </div>
        <div class="ai-grid">
            <div class="ai-card">
                <span class="tier-badge">TIER 1 - EXECUTIVE</span>
                <h3>Master Risk Controller</h3>
                <p>Portfolio-wide risk oversight and position limits with real-time monitoring across all trading strategies.</p>
            </div>
            <div class="ai-card">
                <span class="tier-badge">TIER 1 - EXECUTIVE</span>
                <h3>Strategic Asset Allocator</h3>
                <p>High-level asset allocation and rebalancing decisions based on market conditions and risk parameters.</p>
            </div>
            <div class="ai-card">
                <span class="tier-badge">TIER 1 - EXECUTIVE</span>
                <h3>Performance Monitor</h3>
                <p>Real-time P&L tracking and performance attribution across all agents and trading strategies.</p>
            </div>
            <div class="ai-card">
                <span class="tier-badge">TIER 2 - STRATEGIC</span>
                <h3>Equity Trading Agent</h3>
                <p>Stock selection and equity market execution with advanced order routing and market impact optimization.</p>
            </div>
            <div class="ai-card">
                <span class="tier-badge">TIER 2 - STRATEGIC</span>
                <h3>Fixed Income Agent</h3>
                <p>Bond trading and yield curve strategies with duration matching and credit risk assessment.</p>
            </div>
            <div class="ai-card">
                <span class="tier-badge">TIER 2 - STRATEGIC</span>
                <h3>FX Trading Agent</h3>
                <p>Currency pairs and cross-currency hedging with real-time volatility adjustment and carry optimization.</p>
            </div>
            <div class="ai-card">
                <span class="tier-badge">TIER 3 - TACTICAL</span>
                <h3>Momentum Strategy Agent</h3>
                <p>Trend-following and momentum signals across multiple timeframes and asset classes.</p>
            </div>
            <div class="ai-card">
                <span class="tier-badge">TIER 3 - TACTICAL</span>
                <h3>Mean Reversion Agent</h3>
                <p>Statistical arbitrage and pairs trading with cointegration analysis and risk-adjusted positioning.</p>
            </div>
            <div class="ai-card">
                <span class="tier-badge">TIER 3 - TACTICAL</span>
                <h3>Event-Driven Agent</h3>
                <p>Earnings, M&A, and corporate actions with sentiment analysis and event probability modeling.</p>
            </div>
            <div class="ai-card">
                <span class="tier-badge">TIER 4 - ANALYTICAL</span>
                <h3>News Sentiment Agent</h3>
                <p>Real-time news analysis and sentiment scoring with natural language processing and market impact prediction.</p>
            </div>
            <div class="ai-card">
                <span class="tier-badge">TIER 4 - ANALYTICAL</span>
                <h3>Technical Analysis Agent</h3>
                <p>Chart patterns and technical indicators with machine learning pattern recognition and signal optimization.</p>
            </div>
            <div class="ai-card">
                <span class="tier-badge">TIER 4 - ANALYTICAL</span>
                <h3>Options Flow Agent</h3>
                <p>Derivatives flow and volatility analysis with gamma hedging and options market making strategies.</p>
            </div>
            <div class="ai-card">
                <span class="tier-badge">TIER 4 - ANALYTICAL</span>
                <h3>Economic Data Agent</h3>
                <p>Macro indicators and central bank communications with economic model forecasting and policy impact analysis.</p>
            </div>
            <div class="ai-card">
                <span class="tier-badge">TIER 5 - EXECUTION</span>
                <h3>Smart Order Router</h3>
                <p>Intelligent order routing and execution algorithms with slippage minimization and market impact optimization.</p>
            </div>
            <div class="ai-card">
                <span class="tier-badge">TIER 5 - EXECUTION</span>
                <h3>Risk Management System</h3>
                <p>Real-time position monitoring and automated risk controls with portfolio-level stop-loss and hedging mechanisms.</p>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# Blue Innovation Section
st.markdown("""
<section class="blue-section">
    <div class="section-container">
        <div class="section-split">
            <div class="content-left">
                <h2>More Than 5 Years of AI Innovation</h2>
            </div>
            <div class="content-right">
                <p>Together, we've imagined, innovated and created a next-generation AI platform that operates at global scale.</p>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# Team Excellence Section with GS-Style Background
st.markdown("""
<section class="team-section" style="background: linear-gradient(135deg, rgba(26, 54, 93, 0.95) 0%, rgba(45, 90, 160, 0.9) 100%), url('https://images.unsplash.com/photo-1497366216548-37526070297c?w=1200&auto=format&fit=crop&q=80'); background-size: cover; background-position: center; color: white; position: relative;">
    <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: rgba(26, 54, 93, 0.85); z-index: 1;"></div>
    <div class="section-container" style="position: relative; z-index: 2;">
        <div class="section-split">
            <div class="content-left">
                <h2 style="color: white; margin-bottom: 32px;">Extraordinary AI. Exceptional Intelligence.</h2>
                <div style="position: relative; border-radius: 12px; overflow: hidden; box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);">
                    <img src="https://images.unsplash.com/photo-1552664730-d307ca884978?w=800&auto=format&fit=crop&q=80" 
                         alt="Professional Team Meeting" 
                         style="width: 100%; height: 300px; object-fit: cover;">
                    <div style="position: absolute; bottom: 0; left: 0; right: 0; background: linear-gradient(transparent, rgba(0, 0, 0, 0.7)); padding: 20px; color: white;">
                        <div style="font-size: 14px; font-weight: 500;">Global Excellence • Institutional Standards</div>
                    </div>
                </div>
            </div>
            <div class="content-right">
                <p style="color: rgba(255, 255, 255, 0.9); font-size: 20px; line-height: 1.7;">Our people succeed as a system. The brightest minds across a range of disciplines collaborate to realize our ambitions. We always seek a better way, and we're just getting started.</p>
                <p style="color: rgba(255, 255, 255, 0.8); font-size: 16px; margin-top: 24px;">For more than five years, we've captured undiscovered market opportunities by empowering extraordinary people to pursue their best and boldest ideas.</p>
            </div>
        </div>
        <div class="team-stats" style="margin-top: 80px;">
            <div style="text-align: center; padding: 40px 20px; background: rgba(255, 255, 255, 0.1); border-radius: 12px; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.2);">
                <div style="font-size: 42px; font-weight: 700; color: #60a5fa; margin-bottom: 12px;">45%</div>
                <div style="font-size: 14px; color: rgba(255, 255, 255, 0.8); font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px;">Advanced Degrees</div>
            </div>
            <div style="text-align: center; padding: 40px 20px; background: rgba(255, 255, 255, 0.1); border-radius: 12px; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.2);">
                <div style="font-size: 42px; font-weight: 700; color: #60a5fa; margin-bottom: 12px;">260+</div>
                <div style="font-size: 14px; color: rgba(255, 255, 255, 0.8); font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px;">Universities Represented</div>
            </div>
            <div style="text-align: center; padding: 40px 20px; background: rgba(255, 255, 255, 0.1); border-radius: 12px; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.2);">
                <div style="font-size: 42px; font-weight: 700; color: #60a5fa; margin-bottom: 12px;">60+</div>
                <div style="font-size: 14px; color: rgba(255, 255, 255, 0.8); font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px;">Countries of Origin</div>
            </div>
            <div style="text-align: center; padding: 40px 20px; background: rgba(255, 255, 255, 0.1); border-radius: 12px; box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.2);">
                <div style="font-size: 42px; font-weight: 700; color: #60a5fa; margin-bottom: 12px;">15</div>
                <div style="font-size: 14px; color: rgba(255, 255, 255, 0.8); font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px;">AI Trading Agents</div>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# Additional Content Section with Better Contrast
st.markdown("""
<section class="content-section" style="background: linear-gradient(135deg, #f8fafb 0%, #e8f2f6 100%);">
    <div class="section-container">
        <div class="section-split">
            <div class="content-left">
                <div style="background: linear-gradient(135deg, #1a365d 0%, #2d5aa0 100%); border-radius: 12px; padding: 20px; position: relative; overflow: hidden;">
                    <img src="https://images.unsplash.com/photo-1590479773265-7464e5d48118?w=800&auto=format&fit=crop&q=80" 
                         alt="Professional Trading Technology" 
                         style="width: 100%; height: 350px; object-fit: cover; border-radius: 8px; opacity: 0.85;">
                    <div style="position: absolute; top: 20px; left: 20px; background: rgba(255, 255, 255, 0.95); padding: 12px 20px; border-radius: 6px;">
                        <div style="color: #1a365d; font-weight: 600; font-size: 16px;">LIVE MARKET DATA</div>
                        <div style="color: #2d5aa0; font-size: 14px;">Real-time Processing</div>
                    </div>
                    <div style="position: absolute; bottom: 20px; right: 20px; background: rgba(0, 123, 255, 0.9); color: white; padding: 8px 16px; border-radius: 4px; font-size: 14px; font-weight: 500;">
                        ↗ +18.7% YTD
                    </div>
                </div>
            </div>
            <div class="content-right">
                <h2 style="color: #1a365d;">Institutional-Grade Infrastructure</h2>
                <p style="color: #4a5568;">Our technology infrastructure is built to institutional standards with 99.99% uptime, microsecond latency, and enterprise-grade security.</p>
                <p style="color: #4a5568;">Direct market access, prime brokerage relationships, and regulatory compliance across global markets ensure seamless operations for our institutional clients.</p>
                <a href="#insights" class="citadel-cta">Learn More About Our Technology</a>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# Footer
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
