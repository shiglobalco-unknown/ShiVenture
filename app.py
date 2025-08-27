"""
Shi Ventures - Professional Institutional AI Hedge Fund Website
Domain: shiventure.com
"""

import streamlit as st
import time
import numpy as np
from datetime import datetime
import pandas as pd

# Page config
st.set_page_config(
    page_title="Shi Ventures - Institutional AI Investment Management",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Professional CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    .stApp {
        background: #ffffff;
    }
    
    /* Remove Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stApp > header {visibility: hidden;}
    .stDeployButton {visibility: hidden;}
    .stActionButton {visibility: hidden;}
    div[data-testid="stToolbar"] {visibility: hidden;}
    div[data-testid="stDecoration"] {visibility: hidden;}
    
    /* Navigation */
    .nav-container {
        background: rgba(255, 255, 255, 0.98);
        backdrop-filter: blur(20px);
        border-bottom: 1px solid #e2e8f0;
        padding: 1rem 0;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    }
    
    .nav-content {
        max-width: 1200px;
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 2rem;
    }
    
    .logo {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1a202c;
        text-decoration: none;
    }
    
    .nav-links {
        display: flex;
        gap: 2rem;
    }
    
    .nav-link {
        color: #4a5568;
        text-decoration: none;
        font-weight: 500;
        transition: color 0.2s;
    }
    
    .nav-link:hover {
        color: #1a202c;
    }
    
    .client-access {
        background: #1a202c;
        color: white;
        padding: 0.6rem 1.2rem;
        border-radius: 6px;
        text-decoration: none;
        font-weight: 500;
        transition: all 0.2s;
        border: none;
        cursor: pointer;
    }
    
    .client-access:hover {
        background: #2d3748;
        color: white;
        transform: translateY(-1px);
    }
    
    /* Hero Section */
    .hero {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
        min-height: 100vh;
        display: flex;
        align-items: center;
        padding: 8rem 2rem 4rem 2rem;
        position: relative;
    }
    
    .hero::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grid" width="10" height="10" patternUnits="userSpaceOnUse"><path d="M 10 0 L 0 0 0 10" fill="none" stroke="%23cbd5e0" stroke-width="0.5" opacity="0.3"/></pattern></defs><rect width="100" height="100" fill="url(%23grid)"/></svg>');
        opacity: 0.4;
    }
    
    .hero-content {
        max-width: 1200px;
        margin: 0 auto;
        text-align: center;
        position: relative;
        z-index: 2;
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 800;
        color: #1a202c;
        margin-bottom: 1.5rem;
        line-height: 1.1;
        letter-spacing: -0.02em;
    }
    
    .hero-subtitle {
        font-size: 1.25rem;
        color: #718096;
        font-weight: 400;
        margin-bottom: 3rem;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
        line-height: 1.6;
    }
    
    .hero-cta {
        background: #1a202c;
        color: white;
        padding: 1rem 2rem;
        border-radius: 6px;
        text-decoration: none;
        font-weight: 600;
        font-size: 1.1rem;
        display: inline-block;
        transition: all 0.2s;
        border: none;
        cursor: pointer;
    }
    
    .hero-cta:hover {
        background: #2d3748;
        transform: translateY(-2px);
        color: white;
    }
    
    /* Stats Section */
    .stats {
        background: white;
        padding: 6rem 2rem;
        border-top: 1px solid #e2e8f0;
    }
    
    .stats-container {
        max-width: 1200px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 3rem;
    }
    
    .stat {
        text-align: center;
        padding: 2rem 1rem;
        background: white;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
        transition: all 0.2s;
    }
    
    .stat:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
    }
    
    .stat-number {
        font-size: 3rem;
        font-weight: 800;
        color: #1a202c;
        margin-bottom: 0.5rem;
        line-height: 1;
    }
    
    .stat-label {
        font-size: 0.9rem;
        color: #718096;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }
    
    /* Content Sections */
    .section {
        padding: 6rem 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .section-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1a202c;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    .section-subtitle {
        font-size: 1.1rem;
        color: #718096;
        text-align: center;
        max-width: 700px;
        margin: 0 auto 3rem auto;
        line-height: 1.6;
    }
    
    /* Agent Grid */
    .agents-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin-top: 3rem;
    }
    
    .agent-card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 2rem;
        transition: all 0.3s;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    }
    
    .agent-card:hover {
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
        transform: translateY(-5px);
        border-color: #cbd5e0;
    }
    
    .agent-name {
        font-size: 1.1rem;
        font-weight: 600;
        color: #1a202c;
        margin-bottom: 0.5rem;
    }
    
    .agent-tier {
        font-size: 0.8rem;
        color: #718096;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 1rem;
    }
    
    .agent-performance {
        font-size: 2rem;
        font-weight: 700;
        color: #38a169;
        margin-bottom: 0.5rem;
    }
    
    .agent-status {
        font-size: 0.9rem;
        color: #718096;
    }
    
    /* Content Cards */
    .content-card {
        padding: 2rem;
        background: #f7fafc;
        border-radius: 8px;
        margin-bottom: 2rem;
        border-left: 4px solid #4299e1;
    }
    
    .content-card h3 {
        color: #1a202c;
        margin-bottom: 1rem;
        font-weight: 600;
    }
    
    .content-card p {
        color: #718096;
        line-height: 1.6;
        margin: 0;
    }
    
    /* Footer */
    .footer {
        background: #1a202c;
        color: white;
        padding: 4rem 2rem 2rem 2rem;
    }
    
    .footer-content {
        max-width: 1200px;
        margin: 0 auto;
        text-align: center;
    }
    
    .footer-title {
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 2rem;
    }
    
    .footer-links {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin-bottom: 2rem;
        flex-wrap: wrap;
    }
    
    .footer-link {
        color: #a0aec0;
        text-decoration: none;
        font-weight: 500;
        transition: color 0.2s;
    }
    
    .footer-link:hover {
        color: white;
    }
    
    .footer-bottom {
        border-top: 1px solid #2d3748;
        padding-top: 2rem;
        margin-top: 2rem;
        color: #a0aec0;
        font-size: 0.9rem;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
        }
        
        .stats-container {
            grid-template-columns: repeat(2, 1fr);
            gap: 2rem;
        }
        
        .nav-links {
            display: none;
        }
        
        .hero-subtitle {
            font-size: 1.1rem;
        }
        
        .section-title {
            font-size: 2rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Navigation
st.markdown("""
<div class="nav-container">
    <div class="nav-content">
        <a href="#" class="logo">Shi Ventures</a>
        <div class="nav-links">
            <a href="#about" class="nav-link">About</a>
            <a href="#strategies" class="nav-link">Strategies</a>
            <a href="#performance" class="nav-link">Performance</a>
            <a href="#contact" class="nav-link">Contact</a>
        </div>
        <a href="#" class="client-access">Client Access</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero">
    <div class="hero-content">
        <h1 class="hero-title">Institutional AI Investment Management</h1>
        <p class="hero-subtitle">
            Advanced artificial intelligence meets institutional precision. 
            Our 15-agent system delivers consistent alpha through sophisticated quantitative strategies and real-time market adaptation.
        </p>
        <a href="#about" class="hero-cta">Explore Our Approach</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Demo agent data (since we can't import the API directly)
demo_agents = [
    {"name": "CEO Agent", "tier": "Executive", "performance": 96.2, "last_action": "2 min ago"},
    {"name": "Strategic Command Center", "tier": "Strategic", "performance": 94.1, "last_action": "30 sec ago"},
    {"name": "Strategy Evolution Agent", "tier": "Strategic", "performance": 93.8, "last_action": "1 min ago"},
    {"name": "Fund Optimization Agent", "tier": "Strategic", "performance": 95.2, "last_action": "45 sec ago"},
    {"name": "Quant Director", "tier": "Director", "performance": 94.8, "last_action": "1 min ago"},
    {"name": "Trading Director", "tier": "Director", "performance": 93.5, "last_action": "20 sec ago"},
    {"name": "Risk Director", "tier": "Director", "performance": 97.1, "last_action": "45 sec ago"},
    {"name": "Mathematical Modeler", "tier": "Specialist", "performance": 91.3, "last_action": "1 min ago"},
    {"name": "Execution Agent", "tier": "Specialist", "performance": 91.2, "last_action": "5 sec ago"}
]

# Stats Section
st.markdown("""
<div class="stats">
    <div class="stats-container">
        <div class="stat">
            <div class="stat-number">$66.8M</div>
            <div class="stat-label">Assets Under Management</div>
        </div>
        <div class="stat">
            <div class="stat-number">15</div>
            <div class="stat-label">AI Agents Active</div>
        </div>
        <div class="stat">
            <div class="stat-number">94.2%</div>
            <div class="stat-label">System Performance</div>
        </div>
        <div class="stat">
            <div class="stat-number">+18.7%</div>
            <div class="stat-label">YTD Returns</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# AI System Section
st.markdown("""
<div class="section" id="about">
    <h2 class="section-title">AI Agent System</h2>
    <p class="section-subtitle">
        Our sophisticated 15-agent architecture operates with institutional precision, 
        delivering consistent performance through advanced coordination and real-time market adaptation.
    </p>
</div>
""", unsafe_allow_html=True)

# Agent Grid
cols = st.columns(3)
for i, agent in enumerate(demo_agents):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="agent-card">
            <div class="agent-name">{agent['name']}</div>
            <div class="agent-tier">{agent['tier']} Tier</div>
            <div class="agent-performance">{agent['performance']:.1f}%</div>
            <div class="agent-status">Active • {agent['last_action']}</div>
        </div>
        """, unsafe_allow_html=True)

# About Section
st.markdown("""
<div class="section" id="strategies">
    <h2 class="section-title">Institutional Excellence</h2>
    <p class="section-subtitle">
        Combining deep quantitative expertise with cutting-edge artificial intelligence, 
        we deliver institutional-grade investment solutions for sophisticated investors.
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="content-card">
        <h3>Advanced Technology</h3>
        <p>
            Our proprietary AI system processes vast amounts of market data in real-time, 
            identifying opportunities and managing risk with institutional precision.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="content-card">
        <h3>Proven Performance</h3>
        <p>
            Consistent alpha generation through sophisticated quantitative models 
            and optimized execution strategies tailored for institutional investors.
        </p>
    </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="content-card">
        <h3>Risk Management</h3>
        <p>
            Multi-tier risk management system with real-time monitoring and automated 
            position adjustments to protect capital in all market conditions.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="content-card">
        <h3>Institutional Focus</h3>
        <p>
            Designed specifically for institutional investors with sophisticated 
            reporting, compliance tools, and dedicated relationship management.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer" id="contact">
    <div class="footer-content">
        <h3 class="footer-title">Shi Ventures</h3>
        <div class="footer-links">
            <a href="#" class="footer-link">Privacy Policy</a>
            <a href="#" class="footer-link">Terms of Service</a>
            <a href="#" class="footer-link">Investment Disclosures</a>
            <a href="#" class="footer-link">Contact</a>
            <a href="#" class="footer-link">Careers</a>
        </div>
        <div class="footer-bottom">
            <p>© 2024 Shi Ventures. All rights reserved.</p>
            <p>Investment advisory services provided by registered investment advisors.</p>
            <p>This website and its content are for informational purposes only and do not constitute investment advice.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)