"""
Shi Ventures - Professional Hedge Fund Landing Page
Institutional-grade presentation without sensitive performance data
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

# Professional Landing Page CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
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
    div[data-testid="stStatusWidget"] {visibility: hidden;}
    
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
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }
    
    .nav-content {
        max-width: 1400px;
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 2rem;
    }
    
    .logo {
        font-size: 1.6rem;
        font-weight: 800;
        color: #1a202c;
        text-decoration: none;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .logo-icon {
        font-size: 1.8rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .nav-links {
        display: flex;
        gap: 2.5rem;
    }
    
    .nav-link {
        color: #4a5568;
        text-decoration: none;
        font-weight: 500;
        transition: all 0.2s;
        position: relative;
        padding: 0.5rem 0;
    }
    
    .nav-link:hover {
        color: #1a202c;
        transform: translateY(-1px);
    }
    
    .nav-link::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 0;
        height: 2px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        transition: width 0.3s ease;
    }
    
    .nav-link:hover::after {
        width: 100%;
    }
    
    .client-access {
        background: linear-gradient(135deg, #1a202c 0%, #2d3748 100%);
        color: white;
        padding: 0.7rem 1.5rem;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s;
        border: none;
        cursor: pointer;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }
    
    .client-access:hover {
        background: linear-gradient(135deg, #2d3748 0%, #4a5568 100%);
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
    }
    
    /* Hero Section */
    .hero {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
        min-height: 100vh;
        display: flex;
        align-items: center;
        padding: 8rem 2rem 4rem 2rem;
        position: relative;
        overflow: hidden;
    }
    
    .hero::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M 20 0 L 0 0 0 20" fill="none" stroke="%23cbd5e0" stroke-width="0.5" opacity="0.2"/></pattern></defs><rect width="100" height="100" fill="url(%23grid)"/></svg>');
        opacity: 0.5;
    }
    
    .hero-content {
        max-width: 1400px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 4rem;
        align-items: center;
        position: relative;
        z-index: 2;
    }
    
    .hero-text {
        padding-right: 2rem;
    }
    
    .hero-title {
        font-size: 4rem;
        font-weight: 900;
        background: linear-gradient(135deg, #1a202c 0%, #2d3748 50%, #4a5568 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1.5rem;
        line-height: 1.1;
        letter-spacing: -0.03em;
    }
    
    .hero-subtitle {
        font-size: 1.3rem;
        color: #718096;
        font-weight: 400;
        margin-bottom: 3rem;
        line-height: 1.6;
    }
    
    .hero-cta {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem 2rem;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s;
        box-shadow: 0 4px 20px rgba(102, 126, 234, 0.3);
    }
    
    .hero-cta:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 30px rgba(102, 126, 234, 0.4);
        color: white;
    }
    
    .hero-stats {
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 3rem;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 16px 48px rgba(0, 0, 0, 0.1);
    }
    
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 2rem;
    }
    
    .stat-item {
        text-align: center;
        padding: 1.5rem;
        background: rgba(255, 255, 255, 0.5);
        border-radius: 12px;
        transition: all 0.3s;
    }
    
    .stat-item:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
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
    
    /* Technology Section */
    .tech-section {
        background: white;
        padding: 6rem 2rem;
        border-top: 1px solid #e2e8f0;
    }
    
    .section-container {
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .section-title {
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 2rem;
        background: linear-gradient(135deg, #1a202c 0%, #4a5568 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .section-subtitle {
        font-size: 1.1rem;
        color: #718096;
        text-align: center;
        max-width: 700px;
        margin: 0 auto 4rem auto;
        line-height: 1.6;
    }
    
    .tech-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
        gap: 3rem;
        margin-top: 4rem;
    }
    
    .tech-card {
        padding: 3rem 2rem;
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
        border-radius: 16px;
        border-left: 4px solid #667eea;
        transition: all 0.3s;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
        text-align: center;
    }
    
    .tech-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 16px 48px rgba(0, 0, 0, 0.15);
        border-left-color: #764ba2;
    }
    
    .tech-icon {
        font-size: 3rem;
        margin-bottom: 1.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .tech-card h3 {
        color: #1a202c;
        margin-bottom: 1rem;
        font-weight: 700;
        font-size: 1.3rem;
    }
    
    .tech-card p {
        color: #718096;
        line-height: 1.7;
        margin: 0;
    }
    
    /* Approach Section */
    .approach-section {
        background: #f8fafc;
        padding: 6rem 2rem;
    }
    
    .approach-content {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 4rem;
        align-items: center;
        margin-top: 3rem;
    }
    
    .approach-text h3 {
        font-size: 2rem;
        font-weight: 700;
        color: #1a202c;
        margin-bottom: 1.5rem;
    }
    
    .approach-text p {
        font-size: 1.1rem;
        color: #718096;
        line-height: 1.7;
        margin-bottom: 1.5rem;
    }
    
    .approach-features {
        list-style: none;
        padding: 0;
    }
    
    .approach-features li {
        display: flex;
        align-items: center;
        margin-bottom: 1rem;
        font-weight: 500;
        color: #4a5568;
    }
    
    .approach-features li::before {
        content: '✓';
        color: #38a169;
        font-weight: bold;
        margin-right: 1rem;
        font-size: 1.2rem;
    }
    
    .approach-visual {
        background: white;
        border-radius: 16px;
        padding: 3rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    
    .agent-hierarchy {
        display: flex;
        flex-direction: column;
        gap: 1rem;
    }
    
    .agent-tier {
        padding: 1rem;
        border-radius: 8px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        font-size: 0.9rem;
    }
    
    .tier-executive { background: #fef3c7; color: #d97706; }
    .tier-strategic { background: #dbeafe; color: #2563eb; }
    .tier-director { background: #e0e7ff; color: #7c3aed; }
    .tier-specialist { background: #d1fae5; color: #059669; }
    .tier-support { background: #f1f5f9; color: #64748b; }
    
    /* Contact Section */
    .contact-section {
        background: linear-gradient(135deg, #1a202c 0%, #2d3748 100%);
        color: white;
        padding: 6rem 2rem;
        text-align: center;
    }
    
    .contact-title {
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 1.5rem;
    }
    
    .contact-subtitle {
        font-size: 1.1rem;
        color: #a0aec0;
        margin-bottom: 3rem;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
        line-height: 1.6;
    }
    
    .contact-cta {
        display: inline-block;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem 2rem;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s;
        box-shadow: 0 4px 20px rgba(102, 126, 234, 0.3);
    }
    
    .contact-cta:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 30px rgba(102, 126, 234, 0.4);
        color: white;
    }
    
    /* Footer */
    .footer {
        background: #1a202c;
        color: white;
        padding: 4rem 2rem 2rem 2rem;
        text-align: center;
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
        border-top: 1px solid #4a5568;
        padding-top: 2rem;
        color: #a0aec0;
        font-size: 0.9rem;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .hero-content {
            grid-template-columns: 1fr;
            text-align: center;
        }
        
        .hero-title {
            font-size: 2.5rem;
        }
        
        .stats-grid {
            grid-template-columns: 1fr;
        }
        
        .nav-links {
            display: none;
        }
        
        .tech-grid {
            grid-template-columns: 1fr;
        }
        
        .approach-content {
            grid-template-columns: 1fr;
        }
    }
</style>
""", unsafe_allow_html=True)

# Navigation
st.markdown("""
<div class="nav-container">
    <div class="nav-content">
        <a href="#" class="logo">
            <span class="logo-icon">⚡</span>
            Shi Ventures
        </a>
        <div class="nav-links">
            <a href="#technology" class="nav-link">Technology</a>
            <a href="#approach" class="nav-link">Our Approach</a>
            <a href="#contact" class="nav-link">Contact</a>
        </div>
        <a href="#" class="client-access">Client Portal</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero">
    <div class="hero-content">
        <div class="hero-text">
            <h1 class="hero-title">Institutional AI Investment Management</h1>
            <p class="hero-subtitle">
                Advanced artificial intelligence meets institutional precision. Our sophisticated 
                multi-agent system delivers consistent results through quantitative strategies and 
                institutional-grade risk management.
            </p>
            <a href="#contact" class="hero-cta">Request Information</a>
        </div>
        
        <div class="hero-stats">
            <div class="stats-grid">
                <div class="stat-item">
                    <div class="stat-number">15</div>
                    <div class="stat-label">AI Agents</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">5</div>
                    <div class="stat-label">Operational Tiers</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">24/7</div>
                    <div class="stat-label">Market Monitoring</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">100%</div>
                    <div class="stat-label">Systematic Process</div>
                </div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Technology Section
st.markdown("""
<div class="tech-section" id="technology">
    <div class="section-container">
        <h2 class="section-title">Advanced AI Technology</h2>
        <p class="section-subtitle">
            Our proprietary artificial intelligence platform combines cutting-edge machine learning 
            with institutional-grade infrastructure to deliver superior investment outcomes.
        </p>
        
        <div class="tech-grid">
            <div class="tech-card">
                <div class="tech-icon">🧠</div>
                <h3>Multi-Agent Architecture</h3>
                <p>
                    Sophisticated 15-agent system with specialized roles across executive, strategic, 
                    directorial, specialist, and support tiers for comprehensive market coverage.
                </p>
            </div>
            <div class="tech-card">
                <div class="tech-icon">⚡</div>
                <h3>Real-Time Processing</h3>
                <p>
                    Advanced computational infrastructure processes vast amounts of market data 
                    instantaneously, identifying opportunities faster than human traders.
                </p>
            </div>
            <div class="tech-card">
                <div class="tech-icon">🛡️</div>
                <h3>Risk Management</h3>
                <p>
                    Multi-layered risk protocols with dynamic hedging, real-time position sizing, 
                    and adaptive portfolio rebalancing based on market conditions.
                </p>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Our Approach Section
st.markdown("""
<div class="approach-section" id="approach">
    <div class="section-container">
        <h2 class="section-title">Our Investment Approach</h2>
        <p class="section-subtitle">
            Combining quantitative excellence with institutional discipline to deliver 
            consistent, risk-adjusted returns for sophisticated investors.
        </p>
        
        <div class="approach-content">
            <div class="approach-text">
                <h3>Systematic Excellence</h3>
                <p>
                    Our investment process removes human emotion and bias through systematic, 
                    data-driven decision making. Every trade is executed based on quantitative 
                    analysis and risk-adjusted expected returns.
                </p>
                <ul class="approach-features">
                    <li>Quantitative signal generation and analysis</li>
                    <li>Dynamic portfolio optimization and rebalancing</li>
                    <li>Advanced risk management and hedging strategies</li>
                    <li>Institutional-grade execution and reporting</li>
                    <li>Continuous model improvement and adaptation</li>
                </ul>
            </div>
            
            <div class="approach-visual">
                <h4 style="color: #1a202c; margin-bottom: 2rem; font-weight: 700;">AI Agent Hierarchy</h4>
                <div class="agent-hierarchy">
                    <div class="agent-tier tier-executive">Executive Tier - Strategic Oversight</div>
                    <div class="agent-tier tier-strategic">Strategic Tier - Fund Optimization</div>
                    <div class="agent-tier tier-director">Director Tier - Operational Management</div>
                    <div class="agent-tier tier-specialist">Specialist Tier - Execution & Analysis</div>
                    <div class="agent-tier tier-support">Support Tier - Market Intelligence</div>
                </div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Contact Section
st.markdown("""
<div class="contact-section" id="contact">
    <div class="section-container">
        <h2 class="contact-title">Partner With Shi Ventures</h2>
        <p class="contact-subtitle">
            Designed for institutional investors and sophisticated individuals seeking 
            superior risk-adjusted returns through advanced artificial intelligence.
        </p>
        <a href="#" class="contact-cta">Schedule Consultation</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <div class="section-container">
        <div class="footer-links">
            <a href="#" class="footer-link">Privacy Policy</a>
            <a href="#" class="footer-link">Terms of Service</a>
            <a href="#" class="footer-link">Investment Disclosures</a>
            <a href="#" class="footer-link">Regulatory Information</a>
            <a href="#" class="footer-link">Contact</a>
        </div>
        <div class="footer-bottom">
            <p>© 2024 Shi Ventures. All rights reserved.</p>
            <p style="margin-top: 0.5rem;">
                Investment advisory services provided by registered investment advisors. 
                Past performance does not guarantee future results. All investments involve risk.
            </p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
