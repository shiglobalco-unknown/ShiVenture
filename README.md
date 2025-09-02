# 🏛️ Shi Ventures - AI Hedge Fund Platform

**Live Site:** [shiventure.com](https://shiventure.com)  
**Professional trading interface with real-time updates and live dashboard**  
**Sanitized for public GitHub repository**

## 🎯 Project Overview

Professional AI hedge fund platform showcasing institutional-grade trading interface design with live updates, real-time data simulation, Charles Schwab-inspired styling, and comprehensive 15-agent AI system visualization.

## 🌟 Features

### **Professional Website**
- Charles Schwab-inspired professional design
- Real-time market data simulation  
- Live updating dashboard with current time
- Mobile-responsive layout
- Professional navigation and branding

### **Trading Dashboard Demo**
- **Live Portfolio Monitoring** - Real-time account values and P&L
- **Current Positions Table** - Active futures positions with live updates
- **Performance Charts** - Portfolio performance visualization  
- **Market Data Panel** - Live market prices for major futures contracts
- **Demo Controls** - Emergency controls and portfolio management preview

### **Real-Time Features**
- **Auto-refresh** - Data updates every 5 seconds automatically
- **Live timestamps** - Current time displayed throughout interface
- **Dynamic data** - Portfolio values and market data change continuously
- **Interactive elements** - Demo trading controls and navigation

## 🚀 Quick Start

### **Installation**

```bash
# Clone the repository
git clone https://github.com/yourusername/shiventures.git
cd shiventures

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

### **Access the Platform**

- **Homepage**: Clean professional landing page
- **Trading Dashboard**: Click "📊 Dashboard" to view demo interface  
- **Login**: Click "🔐 Login" to access professional login page

Visit: http://localhost:8501

## 📊 Demo Features

### **Live Updates**
- Portfolio values update every 5 seconds
- Market data changes in real-time
- Current time displayed with live clock
- Position P&L updates automatically

### **Interactive Elements**  
- Demo emergency controls (Trading Lock, Kill Switch)
- Portfolio refresh functionality
- Market data navigation
- Professional login simulation

## 🏗️ Technical Stack

- **Frontend**: Streamlit with custom CSS
- **Charts**: Plotly for professional visualizations
- **Data**: Pandas and NumPy for data handling  
- **Styling**: Professional CSS following industry standards

## 🛡️ Security Note

This is a **demonstration platform** for showcasing professional trading interface design. All data is simulated for demonstration purposes only.

- No real trading functionality
- No actual API connections  
- No sensitive information stored
- Demo data only

## 📝 Project Structure

```
shiventures/
├── app.py              # Main application with live updates
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
├── components/        # Reusable UI components (future)
├── config/           # Configuration files  
└── static/           # Static assets (future)
```

## 🎯 Development

### **Adding New Features**
- Follow professional coding standards
- Maintain consistent styling
- Keep demo data realistic but fictional
- Preserve live update functionality

### **Customization**
- Modify colors in CSS section
- Update demo data in `generate_demo_data()`
- Add new pages by creating functions and updating navigation
- Extend real-time features by modifying update intervals

## 📈 Live Features

### **Real-Time Data**
```python
# Data updates every 5 seconds automatically
if (datetime.now() - st.session_state.last_update).seconds > 5:
    st.session_state.demo_data = generate_demo_data()
    st.session_state.last_update = datetime.now()
```

### **Live Timestamps**
```python
# Current time displayed throughout interface
current_time = datetime.now().strftime("%H:%M:%S EST")
```

### **Automatic Refresh**
- Portfolio values change dynamically
- Market data updates continuously
- P&L calculations refresh in real-time
- Charts update with new data points

## 🌐 Deployment

Ready for deployment to professional hosting platforms:

- **Streamlit Cloud**: Direct deployment from GitHub
- **Heroku**: Professional application hosting
- **AWS/GCP**: Enterprise-grade deployment  
- **Custom Domain**: Connect to shiventures.com

## ⚖️ Legal

This demonstration platform is for educational and showcase purposes only. No actual financial services are provided.

---

## ✨ Professional AI Hedge Fund Interface

**Experience institutional-grade trading interface design with real-time updates and professional styling.**