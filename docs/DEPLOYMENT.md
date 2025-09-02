# 🚀 Deployment Guide - shiventure.com

## 🎯 Deployment Options

### Option 1: Streamlit Cloud (Recommended)

**Advantages**: Free, automatic HTTPS, easy domain connection, zero server maintenance

#### Steps:
1. **Prepare Repository**
   ```bash
   cd "/Users/anthonyshi/Documents/Cursor Projects/shiventure-website"
   git init
   git add .
   git commit -m "Clean consolidated shiventure.com website"
   git remote add origin https://github.com/shiglobalco-unknown/ShiVenture.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Connect GitHub repository: `shiglobalco-unknown/ShiVenture`
   - Set main file path: `app.py`
   - Click "Deploy"

3. **Connect Custom Domain**
   - In Streamlit Cloud app settings, go to "Settings" → "General"
   - Add custom domain: `shiventure.com`
   - Note the CNAME value provided

4. **Update GoDaddy DNS**
   - Log into GoDaddy Domain Manager
   - Go to DNS settings for shiventure.com
   - Add/Update CNAME record:
     - **Type**: CNAME
     - **Host**: @
     - **Points to**: `share.streamlit.io` (or specific subdomain provided)
     - **TTL**: 600 (10 minutes)

5. **SSL Certificate**
   - Streamlit Cloud automatically provides HTTPS
   - Certificate is managed automatically
   - No additional configuration needed

---

### Option 2: VPS Deployment

**Advantages**: Full control, custom configurations, can run background services

#### Server Setup:
```bash
# On your VPS (Ubuntu/Debian)
sudo apt update
sudo apt install python3 python3-pip nginx certbot python3-certbot-nginx git

# Clone repository
git clone https://github.com/shiglobalco-unknown/ShiVenture.git
cd ShiVenture

# Install dependencies
pip3 install -r config/requirements.txt

# Test locally
streamlit run app.py --server.address=0.0.0.0 --server.port=8501
```

#### Nginx Configuration:
```bash
sudo nano /etc/nginx/sites-available/shiventure.com
```

```nginx
server {
    server_name shiventure.com www.shiventure.com;
    
    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_cache_bypass $http_upgrade;
        proxy_buffering off;
        proxy_read_timeout 86400;
    }
    
    # WebSocket support for Streamlit
    location /_stcore/stream {
        proxy_pass http://localhost:8501/_stcore/stream;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_read_timeout 86400;
    }
}
```

#### Enable Site and SSL:
```bash
# Enable site
sudo ln -s /etc/nginx/sites-available/shiventure.com /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx

# Get SSL certificate
sudo certbot --nginx -d shiventure.com -d www.shiventure.com

# Set up systemd service for Streamlit
sudo nano /etc/systemd/system/shiventure.service
```

```ini
[Unit]
Description=Shiventure Streamlit App
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/ShiVenture
ExecStart=/usr/local/bin/streamlit run app.py --server.address=127.0.0.1 --server.port=8501
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
# Start service
sudo systemctl enable shiventure
sudo systemctl start shiventure
sudo systemctl status shiventure
```

#### GoDaddy DNS for VPS:
- **Type**: A
- **Host**: @
- **Points to**: YOUR_VPS_IP_ADDRESS
- **TTL**: 600

---

## 🔧 Environment Configuration

### Production Environment Variables
Create `.env` file (never commit this):
```bash
# Copy template
cp config/.env.example .env

# Edit with your values
nano .env
```

### Required for Full Functionality:
```env
SITE_URL=https://shiventure.com
DEBUG_MODE=False

# Optional: For enhanced trading features
TOPSTEP_USERNAME=your_topstep_username
TOPSTEP_PASSWORD=your_topstep_password
```

---

## 🧪 Pre-Deployment Testing

### Local Testing Checklist:
```bash
cd "/Users/anthonyshi/Documents/Cursor Projects/shiventure-website"

# 1. Install dependencies
pip install -r config/requirements.txt

# 2. Run local server
streamlit run app.py

# 3. Test main website
# - Navigate to http://localhost:8501
# - Check all sections load properly
# - Verify professional appearance

# 4. Test futures dashboard
# - Click "📊 Futures Dashboard" in navigation
# - Verify emergency controls display
# - Check portfolio management components

# 5. Test navigation
# - Switch between main site and dashboard
# - Ensure smooth transitions
# - Verify session state management
```

### Component Testing:
```bash
# Test emergency controls
python -c "from components.emergency_controls import EmergencyControlSystem; print('✅ Emergency controls OK')"

# Test portfolio manager  
python -c "from components.portfolio_manager import PortfolioManager; print('✅ Portfolio manager OK')"
```

---

## 📊 DNS Propagation

### Check DNS Status:
```bash
# Check if DNS has propagated
nslookup shiventure.com
dig shiventure.com

# Online tools:
# - https://dnschecker.org/
# - https://www.whatsmydns.net/
```

### Typical Propagation Time:
- **GoDaddy**: 1-24 hours
- **Global propagation**: Up to 48 hours
- **TTL setting**: Affects update speed

---

## 🔍 Troubleshooting

### Common Issues:

#### 1. "Module not found" errors:
```bash
# Ensure components directory is accessible
ls -la components/
python -c "import sys; print(sys.path)"
```

#### 2. Streamlit won't start:
```bash
# Check dependencies
pip install -r config/requirements.txt --upgrade

# Check Streamlit version
streamlit version
```

#### 3. Domain not resolving:
- Check DNS settings in GoDaddy
- Verify CNAME/A record configuration  
- Wait for DNS propagation (up to 24 hours)
- Use DNS checker tools

#### 4. HTTPS not working:
- **Streamlit Cloud**: Automatic, wait for provisioning
- **VPS**: Run `sudo certbot renew` and check nginx config

---

## ✅ Go-Live Checklist

### Final Steps:
- [ ] Repository pushed to GitHub
- [ ] Local testing completed successfully
- [ ] Dependencies verified and documented
- [ ] Environment variables configured
- [ ] Deployment method chosen and executed
- [ ] DNS records updated in GoDaddy
- [ ] SSL certificate active (HTTPS working)
- [ ] Main website loads properly
- [ ] Futures dashboard navigation works
- [ ] Emergency controls functional
- [ ] Portfolio management accessible
- [ ] Mobile responsiveness verified

### Post-Launch:
- [ ] Monitor website performance
- [ ] Check for any error logs
- [ ] Verify all features working in production
- [ ] Test from multiple devices/browsers
- [ ] Monitor DNS propagation globally

---

## 🎯 **Ready for shiventure.com Launch!**

Your consolidated website structure is production-ready with professional AI hedge fund presentation and integrated futures portfolio monitoring capabilities.