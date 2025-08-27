"""
Shi Ventures - Exact Citadel Securities Style Replica
1-to-1 professional institutional design matching Citadel's visual standards
"""

import streamlit as st
import time
import numpy as np
from datetime import datetime
import pandas as pd

# Page config
st.set_page_config(
    page_title="Shi Ventures",
    page_icon="🏛️", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Exact Citadel-style CSS
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
    
    .language-selector {
        color: #32373c;
        font-size: 14px;
        cursor: pointer;
    }
    
    /* Hero Section - Citadel Style */
    .citadel-hero {
        background: #ffffff;
        padding-top: 70px;
        min-height: 100vh;
        display: flex;
        align-items: center;
        position: relative;
    }
    
    .hero-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 60px 20px;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 80px;
        align-items: center;
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
        transition: background-color 0.2s ease;
    }
    
    .citadel-cta:hover {
        background: #0056b3;
        color: #ffffff;
    }
    
    .hero-visual {
        background: #f8f9fa;
        border-radius: 8px;
        padding: 40px;
        text-align: center;
    }
    
    .hero-stats {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 30px;
    }
    
    .stat-item {
        text-align: center;
    }
    
    .stat-number {
        font-size: 36px;
        font-weight: 700;
        color: #32373c;
        margin-bottom: 8px;
    }
    
    .stat-label {
        font-size: 14px;
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
    
    .content-right .citadel-cta {
        margin-top: 20px;
    }
    
    /* Stats Section - Citadel Style */
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
    }
    
    .large-stat-number {
        font-size: 72px;
        font-weight: 700;
        color: #007bff;
        margin-bottom: 16px;
        line-height: 1;
    }
    
    .large-stat-label {
        font-size: 16px;
        color: #32373c;
        font-weight: 400;
        line-height: 1.4;
        max-width: 250px;
        margin: 0 auto;
    }
    
    /* Blue Section */
    .blue-section {
        background: #007bff;
        color: #ffffff;
        padding: 100px 20px;
    }
    
    .blue-section .section-split {
        align-items: center;
    }
    
    .blue-section h2 {
        font-size: 42px;
        font-weight: 700;
        color: #ffffff;
        line-height: 1.2;
        margin-bottom: 32px;
        letter-spacing: -1px;
    }
    
    .blue-section p {
        font-size: 18px;
        color: rgba(255, 255, 255, 0.9);
        line-height: 1.7;
    }
    
    /* Team Section */
    .team-section {
        background: #f8f9fa;
        padding: 100px 20px;
    }
    
    .team-section h2 {
        font-size: 42px;
        font-weight: 700;
        color: #32373c;
        line-height: 1.2;
        margin-bottom: 32px;
        letter-spacing: -1px;
    }
    
    .team-section p {
        font-size: 18px;
        color: #666666;
        line-height: 1.7;
        margin-bottom: 24px;
    }
    
    .team-stats {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 40px;
        margin-top: 60px;
    }
    
    .team-stat {
        text-align: left;
    }
    
    .team-stat-number {
        font-size: 48px;
        font-weight: 700;
        color: #007bff;
        margin-bottom: 12px;
    }
    
    .team-stat-label {
        font-size: 14px;
        color: #666666;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* Footer */
    .citadel-footer {
        background: #32373c;
        color: #ffffff;
        padding: 60px 20px 40px 20px;
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
    }
    
    .footer-nav a {
        color: #ffffff;
        text-decoration: none;
        font-size: 16px;
        font-weight: 400;
    }
    
    .footer-nav a:hover {
        color: #cccccc;
    }
    
    .footer-bottom {
        border-top: 1px solid #555555;
        padding-top: 30px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .footer-legal {
        display: flex;
        gap: 30px;
    }
    
    .footer-legal a {
        color: #cccccc;
        text-decoration: none;
        font-size: 14px;
    }
    
    .footer-copyright {
        color: #cccccc;
        font-size: 14px;
    }
    
    .footer-social {
        display: flex;
        gap: 20px;
    }
    
    .footer-social a {
        color: #cccccc;
        font-size: 20px;
        text-decoration: none;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .hero-container, .section-split, .stats-container, .footer-container {
            grid-template-columns: 1fr;
            gap: 40px;
        }
        
        .hero-content h1 {
            font-size: 36px;
        }
        
        .content-left h2, .blue-section h2, .team-section h2 {
            font-size: 32px;
        }
        
        .large-stat-number {
            font-size: 48px;
        }
        
        .nav-menu {
            display: none;
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
            <a href="#approach" class="nav-item">What We Do</a>
            <a href="#insights" class="nav-item">News & Insights</a>
            <a href="#careers" class="nav-item">Careers</a>
            <span class="language-selector">EN ▼</span>
        </div>
    </div>
</nav>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<section class="citadel-hero">
    <div class="hero-container">
        <div class="hero-content">
            <h1>Where Global Markets Evolve</h1>
            <p>Resilient and efficient markets drive economic opportunity. Through our AI trading, research and technology, we move markets forward.</p>
            <a href="#about" class="citadel-cta">Explore Who We Are</a>
        </div>
        <div class="hero-visual">
            <div class="hero-stats">
                <div class="stat-item">
                    <div class="stat-number">15</div>
                    <div class="stat-label">AI Agents</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">5</div>
                    <div class="stat-label">System Tiers</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">24/7</div>
                    <div class="stat-label">Operations</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">100%</div>
                    <div class="stat-label">Systematic</div>
                </div>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# Content Section 1
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
                <a href="#approach" class="citadel-cta">Explore What We Do</a>
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
            <div class="large-stat-number">#1</div>
            <div class="large-stat-label">In U.S. AI trading market making, with ~35% U.S.-listed retail volume executed through our platform</div>
        </div>
        <div class="large-stat">
            <div class="large-stat-number">$66B</div>
            <div class="large-stat-label">in assets executed a day (approximate notional value in 24 hours, excluding swaps)</div>
        </div>
        <div class="large-stat">
            <div class="large-stat-number">8x</div>
            <div class="large-stat-label">years as a Risk Awards Flow Market Maker of the Year, from 2017 to 2024</div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# Blue Section
st.markdown("""
<section class="blue-section" id="approach">
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

# Team Section
st.markdown("""
<section class="team-section">
    <div class="section-container">
        <div class="section-split">
            <div class="content-left">
                <h2>Extraordinary AI. Exceptional Intelligence.</h2>
            </div>
            <div class="content-right">
                <p>Our people succeed as a system. The brightest minds across a range of disciplines collaborate to realize our ambitions. We always seek a better way, and we're just getting started.</p>
            </div>
        </div>
        <div class="team-stats">
            <div class="team-stat">
                <div class="team-stat-number">45%</div>
                <div class="team-stat-label">Advanced degrees</div>
            </div>
            <div class="team-stat">
                <div class="team-stat-number">260+</div>
                <div class="team-stat-label">Universities represented</div>
            </div>
            <div class="team-stat">
                <div class="team-stat-number">60+</div>
                <div class="team-stat-label">Countries of origin</div>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<footer class="citadel-footer">
    <div class="footer-container">
        <div class="footer-left">
            <div class="footer-logo">SHI VENTURES</div>
        </div>
        <div class="footer-right">
            <nav class="footer-nav">
                <a href="#about">Who We Are</a>
                <a href="#approach">What We Do</a>
                <a href="#insights">News & Insights</a>
                <a href="#careers">Careers</a>
            </nav>
        </div>
    </div>
    <div class="footer-bottom">
        <div class="footer-legal">
            <a href="#">Privacy</a>
            <a href="#">Terms of Use</a>
            <a href="#">Notices</a>
            <a href="#">Disclosures</a>
        </div>
        <div class="footer-copyright">
            Copyright © Shi Ventures AI LLC or one of its affiliates. All rights reserved.
        </div>
        <div class="footer-social">
            <a href="#">📱</a>
            <a href="#">👤</a>
            <a href="#">📸</a>
            <a href="#">📺</a>
        </div>
    </div>
    <div style="text-align: center; padding-top: 20px; border-top: 1px solid #555555;">
        <a href="#" style="color: #cccccc; font-size: 12px; text-decoration: underline;">View footnotes for this page.</a>
    </div>
</footer>
""", unsafe_allow_html=True)
