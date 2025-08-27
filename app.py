"""
Shi Ventures - Enhanced Institutional Landing Page
Combines sophisticated design with proper hedge fund presentation
"""

import streamlit as st
import time
import numpy as np
from datetime import datetime
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Page config
st.set_page_config(
    page_title="Shi Ventures - Institutional AI Investment Management",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Enhanced Institutional CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Crimson+Text:wght@400;600&display=swap');
    
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
    
    /* Institutional Header */
    .institutional-header {
        background: linear-gradient(135deg, #001f3f 0%, #003366 50%, #001f3f 100%);
        color: #ffffff;
        padding: 0;
        margin: -1rem -1rem 0 -1rem;
        position: relative;
        overflow: hidden;
        min-height: 100vh;
        display: flex;
        flex-direction: column;
    }
    
    .header-video {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        opacity: 0.3;
        z-index: 1;
    }
    
    .header-overlay {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, rgba(0, 31, 63, 0.8) 0%, rgba(0, 51, 102, 0.6) 50%, rgba(0, 31, 63, 0.8) 100%);
        z-index: 2;
    }
    
    .header-pattern {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grid" width="10" height="10" patternUnits="userSpaceOnUse"><path d="M 10 0 L 0 0 0 10" fill="none" stroke="%23ffffff" stroke-width="0.5" opacity="0.05"/></pattern></defs><rect width="100" height="100" fill="url(%23grid)"/></svg>');
        opacity: 0.3;
    }
    
    .header-nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px 60px;
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(20px);
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        position: relative;
        z-index: 100;
    }
    
    .logo {
        font-family: 'Crimson Text', serif;
        font-size: 1.8rem;
        font-weight: 600;
        color: #ffffff;
        text-decoration: none;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .logo-icon {
        font-size: 2rem;
        background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .nav-links {
        display: flex;
        gap: 2.5rem;
        align-items: center;
    }
    
    .nav-link {
        color: rgba(255, 255, 255, 0.9);
        text-decoration: none;
        font-weight: 500;
        font-size: 0.95rem;
        transition: all 0.3s ease;
        position: relative;
        padding: 0.5rem 0;
    }
    
    .nav-link:hover {
        color: #ffffff;
        transform: translateY(-1px);
    }
    
    .nav-link::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 0;
        height: 2px;
        background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%);
        transition: width 0.3s ease;
    }
    
    .nav-link:hover::after {
        width: 100%;
    }
    
    .client-portal-btn {
        background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%);
        color: white;
        padding: 12px 24px;
        border-radius: 6px;
        text-decoration: none;
        font-weight: 600;
        font-size: 0.95rem;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
    }
    
    .client-portal-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.4);
        color: white;
    }
    
    /* Hero Content */
    .hero-content {
        flex: 1;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 4rem 60px;
        position: relative;
        z-index: 10;
    }
    
    .hero-container {
        max-width: 1400px;
        width: 100%;
        display: grid;
        grid-template-columns: 1.2fr 0.8fr;
        gap: 6rem;
        align-items: center;
    }
    
    .hero-text {
        color: #ffffff;
    }
    
    .hero-title {
        font-size: 4.5rem;
        font-weight: 900;
        line-height: 1.1;
        margin-bottom: 2rem;
        background: linear-gradient(135deg, #ffffff 0%, #e2e8f0 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -0.02em;
    }
    
    .hero-subtitle {
        font-size: 1.4rem;
        line-height: 1.6;
        color: rgba(255, 255, 255, 0.9);
        margin-bottom: 3rem;
        font-weight: 400;
    }
    
    .hero-cta {
        display: inline-block;
        background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%);
        color: white;
        padding: 16px 32px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.3);
    }
    
    .hero-cta:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(59, 130, 246, 0.4);
        color: white;
    }
    
    /* Hero Stats Panel */
    .hero-stats {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 20px;
        padding: 3rem;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.2);
    }
    
    .stats-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 2rem;
    }
    
    .stat-item {
        text-align: center;
        padding: 1.5rem;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
    }
    
    .stat-item:hover {
        background: rgba(255, 255, 255, 0.1);
        transform: translateY(-5px);
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 800;
        color: #60a5fa;
        margin-bottom: 0.5rem;
        line-height: 1;
    }
    
    .stat-label {
        font-size: 0.9rem;
        color: rgba(255, 255, 255, 0.8);
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }
    
    /* Technology Section */
    .tech-section {
        background: #f8fafc;
        padding: 8rem 60px;
        position: relative;
    }
    
    .section-container {
        max-width: 1400px;
        margin: 0 auto;
    }
    
    .section-header {
        text-align: center;
        margin-bottom: 5rem;
    }
    
    .section-title {
        font-size: 3.5rem;
        font-weight: 800;
        color: #1a202c;
        margin-bottom: 2rem;
        background: linear-gradient(135deg, #1a202c 0%, #4a5568 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .section-subtitle {
        font-size: 1.3rem;
        color: #718096;
        max-width: 800px;
        margin: 0 auto;
        line-height: 1.7;
    }
    
    .tech-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
        gap: 3rem;
    }
    
    .tech-card {
        background: #ffffff;
        border-radius: 20px;
        padding: 3rem;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
        border: 1px solid #e2e8f0;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
    }
    
    .tech-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%);
    }
    
    .tech-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 25px 60px rgba(0, 0, 0, 0.2);
    }
    
    .tech-icon {
        width: 80px;
        height: 80px;
        margin-bottom: 2rem;
        border-radius: 12px;
        background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2rem;
        color: white;
    }
    
    .tech-image {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 12px;
        margin-bottom: 2rem;
    }
    
    .tech-card h3 {
        font-size: 1.8rem;
        font-weight: 700;
        color: #1a202c;
        margin-bottom: 1.5rem;
    }
    
    .tech-card p {
        font-size: 1.1rem;
        color: #718096;
        line-height: 1.7;
        margin-bottom: 2rem;
    }
    
    .tech-features {
        list-style: none;
        padding: 0;
    }
    
    .tech-features li {
        display: flex;
        align-items: center;
        margin-bottom: 1rem;
        font-weight: 500;
        color: #4a5568;
    }
    
    .tech-features li::before {
        content: '✓';
        color: #3b82f6;
        font-weight: bold;
        margin-right: 1rem;
        font-size: 1.2rem;
    }
    
    /* Agent System Section */
    .agent-section {
        background: #ffffff;
        padding: 8rem 60px;
    }
    
    .agent-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
        gap: 2.5rem;
        margin-top: 4rem;
    }
    
    .agent-card {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
        border-radius: 16px;
        padding: 2.5rem;
        border-left: 5px solid #3b82f6;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .agent-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.15);
        background: linear-gradient(135deg, #ffffff 0%, #f1f5f9 100%);
    }
    
    .agent-tier {
        font-size: 0.8rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        margin-bottom: 1rem;
        display: inline-block;
    }
    
    .tier-executive { background: #fef3c7; color: #d97706; }
    .tier-strategic { background: #dbeafe; color: #2563eb; }
    .tier-director { background: #e0e7ff; color: #7c3aed; }
    .tier-specialist { background: #d1fae5; color: #059669; }
    .tier-support { background: #f1f5f9; color: #64748b; }
    
    .agent-name {
        font-size: 1.3rem;
        font-weight: 700;
        color: #1a202c;
        margin-bottom: 1rem;
    }
    
    .agent-description {
        font-size: 1rem;
        color: #718096;
        line-height: 1.6;
        margin-bottom: 1.5rem;
    }
    
    .agent-metrics {
        display: flex;
        justify-content: space-between;
        padding-top: 1.5rem;
        border-top: 1px solid rgba(0, 0, 0, 0.1);
    }
    
    .agent-metric {
        text-align: center;
    }
    
    .metric-value {
        font-size: 1.5rem;
        font-weight: 700;
        color: #3b82f6;
        margin-bottom: 0.25rem;
    }
    
    .metric-label {
        font-size: 0.8rem;
        color: #718096;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    /* Contact Section */
    .contact-section {
        background: linear-gradient(135deg, #1a202c 0%, #2d3748 100%);
        color: #ffffff;
        padding: 8rem 60px;
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    
    .contact-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="dots" width="20" height="20" patternUnits="userSpaceOnUse"><circle cx="10" cy="10" r="1" fill="%23ffffff" opacity="0.1"/></pattern></defs><rect width="100" height="100" fill="url(%23dots)"/></svg>');
        opacity: 0.3;
    }
    
    .contact-content {
        max-width: 800px;
        margin: 0 auto;
        position: relative;
        z-index: 10;
    }
    
    .contact-title {
        font-size: 3.5rem;
        font-weight: 800;
        margin-bottom: 2rem;
        background: linear-gradient(135deg, #ffffff 0%, #e2e8f0 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .contact-subtitle {
        font-size: 1.3rem;
        color: rgba(255, 255, 255, 0.9);
        margin-bottom: 3rem;
        line-height: 1.6;
    }
    
    .contact-cta {
        display: inline-block;
        background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%);
        color: white;
        padding: 18px 36px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: 600;
        font-size: 1.2rem;
        transition: all 0.3s ease;
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.3);
    }
    
    .contact-cta:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(59, 130, 246, 0.4);
        color: white;
    }
    
    /* Footer */
    .footer {
        background: #1a202c;
        color: #ffffff;
        padding: 4rem 60px 2rem 60px;
        text-align: center;
    }
    
    .footer-links {
        display: flex;
        justify-content: center;
        gap: 3rem;
        margin-bottom: 3rem;
        flex-wrap: wrap;
    }
    
    .footer-link {
        color: rgba(255, 255, 255, 0.7);
        text-decoration: none;
        font-weight: 500;
        transition: color 0.2s;
    }
    
    .footer-link:hover {
        color: #ffffff;
    }
    
    .footer-bottom {
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        padding-top: 2rem;
        color: rgba(255, 255, 255, 0.6);
        font-size: 0.9rem;
        line-height: 1.6;
    }
    
    /* Responsive Design */
    @media (max-width: 1200px) {
        .hero-container {
            grid-template-columns: 1fr;
            gap: 4rem;
            text-align: center;
        }
        
        .header-nav {
            padding: 20px 30px;
        }
        
        .hero-content {
            padding: 4rem 30px;
        }
        
        .tech-section, .agent-section, .contact-section, .footer {
            padding: 6rem 30px;
        }
    }
    
    @media (max-width: 768px) {
        .hero-title {
            font-size: 3rem;
        }
        
        .nav-links {
            display: none;
        }
        
        .stats-grid {
            grid-template-columns: 1fr;
        }
        
        .tech-grid, .agent-grid {
            grid-template-columns: 1fr;
        }
        
        .section-title {
            font-size: 2.5rem;
        }
        
        .contact-title {
            font-size: 2.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Institutional Header
st.markdown("""
<div class="institutional-header">
    <video class="header-video" autoplay muted loop>
        <source src="https://player.vimeo.com/external/434045526.sd.mp4?s=c27eecc69a27dbc4ff2b87d38afc35f1a9e87c02" type="video/mp4">
    </video>
    <div class="header-overlay"></div>
    <div class="header-pattern"></div>
    <nav class="header-nav">
        <a href="#" class="logo">
            <span class="logo-icon">⚡</span>
            Shi Ventures
        </a>
        <div class="nav-links">
            <a href="#technology" class="nav-link">Technology</a>
            <a href="#agents" class="nav-link">AI System</a>
            <a href="#contact" class="nav-link">Contact</a>
        </div>
        <a href="#" class="client-portal-btn">Client Portal</a>
    </nav>
    
    <div class="hero-content">
        <div class="hero-container">
            <div class="hero-text">
                <h1 class="hero-title">Institutional AI Investment Management</h1>
                <p class="hero-subtitle">
                    Advanced artificial intelligence meets institutional precision. Our sophisticated 
                    15-agent architecture delivers consistent results through quantitative strategies, 
                    real-time market adaptation, and institutional-grade risk management.
                </p>
                <a href="#contact" class="hero-cta">Request Information</a>
            </div>
            
            <div class="hero-stats">
                <h3 class="stats-title">System Overview</h3>
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
</div>
""", unsafe_allow_html=True)

# Technology Section
st.markdown("""
<div class="tech-section" id="technology">
    <div class="section-container">
        <div class="section-header">
            <h2 class="section-title">Advanced AI Technology</h2>
            <p class="section-subtitle">
                Our proprietary artificial intelligence platform combines cutting-edge machine learning 
                with institutional-grade infrastructure to deliver superior investment outcomes.
            </p>
        </div>
        
        <div class="tech-grid">
            <div class="tech-card">
                <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=500&auto=format&fit=crop&q=60" alt="AI Technology" class="tech-image">
                <h3>Multi-Agent Architecture</h3>
                <p>
                    Sophisticated 15-agent system with specialized roles across five operational tiers, 
                    ensuring comprehensive market coverage and optimal decision-making processes.
                </p>
                <ul class="tech-features">
                    <li>Executive oversight and strategic direction</li>
                    <li>Real-time cross-agent coordination</li>
                    <li>Specialized tier-based responsibilities</li>
                    <li>Continuous performance optimization</li>
                </ul>
            </div>
            
            <div class="tech-card">
                <img src="https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=500&auto=format&fit=crop&q=60" alt="Real-Time Trading" class="tech-image">
                <h3>Real-Time Processing</h3>
                <p>
                    Advanced computational infrastructure processes vast amounts of market data 
                    instantaneously, identifying opportunities faster than traditional methods.
                </p>
                <ul class="tech-features">
                    <li>Microsecond execution capabilities</li>
                    <li>High-frequency data processing</li>
                    <li>Advanced pattern recognition</li>
                    <li>Predictive market modeling</li>
                </ul>
            </div>
            
            <div class="tech-card">
                <img src="https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=500&auto=format&fit=crop&q=60" alt="Risk Management" class="tech-image">
                <h3>Risk Management</h3>
                <p>
                    Multi-layered risk protocols with dynamic hedging, real-time position sizing, 
                    and adaptive portfolio rebalancing based on market conditions.
                </p>
                <ul class="tech-features">
                    <li>Dynamic risk assessment</li>
                    <li>Automated position management</li>
                    <li>Stress testing and scenario analysis</li>
                    <li>Compliance monitoring and reporting</li>
                </ul>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# AI Agent System Section
demo_agents = [
    {
        "name": "CEO Agent", 
        "tier": "Executive", 
        "description": "Provides strategic oversight and high-level decision making across all trading operations.",
        "efficiency": "96%",
        "decisions": "1.8K",
        "uptime": "99.9%"
    },
    {
        "name": "Strategic Command Center", 
        "tier": "Strategic", 
        "description": "Coordinates system-wide optimization and strategic fund management initiatives.",
        "efficiency": "94%",
        "decisions": "3.4K", 
        "uptime": "99.8%"
    },
    {
        "name": "Strategy Evolution Agent", 
        "tier": "Strategic", 
        "description": "Continuously adapts and evolves trading strategies based on market conditions.",
        "efficiency": "94%",
        "decisions": "2.2K",
        "uptime": "99.9%"
    },
    {
        "name": "Quant Director", 
        "tier": "Director", 
        "description": "Oversees quantitative analysis and mathematical modeling for all trading decisions.",
        "efficiency": "95%",
        "decisions": "2.8K",
        "uptime": "99.7%"
    },
    {
        "name": "Risk Director", 
        "tier": "Director", 
        "description": "Manages comprehensive risk assessment and portfolio protection protocols.",
        "efficiency": "97%",
        "decisions": "2.6K",
        "uptime": "99.9%"
    },
    {
        "name": "Execution Agent", 
        "tier": "Specialist", 
        "description": "Handles precise trade execution and order management across all market venues.",
        "efficiency": "91%",
        "decisions": "5.7K",
        "uptime": "99.6%"
    }
]

st.markdown("""
<div class="agent-section" id="agents">
    <div class="section-container">
        <div class="section-header">
            <h2 class="section-title">AI Agent System Architecture</h2>
            <p class="section-subtitle">
                Our sophisticated multi-agent ecosystem operates with institutional precision, featuring 
                real-time coordination, adaptive learning, and advanced risk management protocols.
            </p>
        </div>
        
        <div class="agent-grid">
""", unsafe_allow_html=True)

for agent in demo_agents:
    tier_class = f"tier-{agent['tier'].lower()}"
    st.markdown(f"""
        <div class="agent-card">
            <span class="agent-tier {tier_class}">{agent['tier']} Tier</span>
            <h3 class="agent-name">{agent['name']}</h3>
            <p class="agent-description">{agent['description']}</p>
            <div class="agent-metrics">
                <div class="agent-metric">
                    <div class="metric-value">{agent['efficiency']}</div>
                    <div class="metric-label">Efficiency</div>
                </div>
                <div class="agent-metric">
                    <div class="metric-value">{agent['decisions']}</div>
                    <div class="metric-label">Decisions</div>
                </div>
                <div class="agent-metric">
                    <div class="metric-value">{agent['uptime']}</div>
                    <div class="metric-label">Uptime</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("""
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Contact Section
st.markdown("""
<div class="contact-section" id="contact">
    <div class="contact-content">
        <h2 class="contact-title">Partner With Shi Ventures</h2>
        <p class="contact-subtitle">
            Designed for institutional investors and sophisticated individuals seeking 
            superior risk-adjusted returns through advanced artificial intelligence and 
            quantitative investment strategies.
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
            <p style="margin-top: 1rem;">
                Investment advisory services provided by registered investment advisors. 
                Past performance does not guarantee future results. All investments involve risk and may lose value.
                Securities offered through registered broker-dealers.
            </p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
