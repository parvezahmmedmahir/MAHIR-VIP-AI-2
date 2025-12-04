# 🤖 MAHIR VIP AUTO AI - Premium Binary Signals

> **Advanced AI-Powered Binary Options Signal Generator**  
> Powered by the Three Black Crows Strategy with Smart Money Concepts

---

## 🌟 Features

### 🎯 AI-Powered Signals
- **Real-time Market Analysis** using Python backend
- **Three Black Crows Strategy** implementation
- **Technical Indicators**: RSI, SMA, Market Structure Analysis
- **Confidence Scoring** for each signal (60-95%)
- **1-Minute Expiry** optimized for quick trades

### 🛡️ Safety & Risk Management
- **Safety Margin**: 15-20% buffer on all signals
- **One-Step MTG**: Fixed stake, no martingale
- **Smart Money Concepts** integration
- **Support/Resistance Zone** detection

### 💎 Premium Interface
- **Password Protected** (Password: `MAHIR`)
- **Real-time Countdown** (30-second intervals)
- **Animated Background** with floating shapes
- **Gold/VIP Color Scheme**
- **Mobile Responsive** design

### 📊 Supported Markets
62+ Market Pairs including:
- **OTC Currencies**: NZDCAD_OTC, USDCHF_OTC, USDBRL_OTC, etc.
- **Crypto**: BTCUSD_OTC, SHIBA_OTC, PEPE_OTC, DOGE_OTC, etc.
- **Stocks**: BOEING_OTC, FB-OTC, MSFT_OTC, INTC_OTC, etc.
- **Commodities**: XAUUSD_OTC (Gold), XAGUSD_OTC (Silver)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Modern web browser (Chrome, Firefox, Edge)
- Internet connection

### Installation

1. **Clone or Download** the repository
   ```bash
   cd MAHIR-VIP-AI-1
   ```

2. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Backend Server**
   ```bash
   python main.py
   ```
   
   You should see:
   ```
   Starting MAHIR VIP AUTO AI Server...
   Initializing API connection...
   Connected successfully!
   * Running on http://127.0.0.1:5000
   ```

4. **Open the Frontend**
   - Open `INDEX.HTML` in your web browser
   - Enter password: `MAHIR`
   - Click "GENERATE SIGNAL" to get AI-powered signals

---

## 📁 Project Structure

```
MAHIR-VIP-AI-1/
├── INDEX.HTML              # Main frontend application
├── main.py                 # Flask backend server
├── quotex_api.py          # Market analysis & signal generation logic
├── config.py              # Configuration (assets, strategy settings)
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── THREE_BLACK_CROWS_STRATEGY.md  # Strategy documentation
└── vercel.json            # Vercel deployment config
```

---

## 🎓 Strategy: Three Black Crows

The **Three Black Crows** is a bearish reversal pattern consisting of three consecutive bearish candles, each closing lower than the previous one.

### Signal Generation Logic

1. **Pattern Detection**: Identifies Three Black Crows formation
2. **RSI Analysis**: 
   - RSI < 30 → Oversold (CALL signal)
   - RSI > 70 → Overbought (PUT signal)
3. **Trend Analysis**: Compares current price with 20-period SMA
4. **Confidence Scoring**: 
   - Three Black Crows detected: 95% confidence
   - RSI extreme: 85% confidence
   - Trend following: 75% confidence

### Risk Management

- **Safety Margin**: 15-20% buffer on entry price
- **One-Step MTG**: No martingale, fixed stake per trade
- **1-Minute Expiry**: Quick execution, minimal exposure

---

## 🔧 Configuration

### Customization Options

#### Change Password
Edit `INDEX.HTML` line ~2115:
```javascript
const correctPassword = "YOUR_PASSWORD";
```

#### Adjust Countdown Timer
Edit `INDEX.HTML` line ~2114:
```javascript
let countdownTime = 30; // seconds
```

#### Modify Market Pairs
Edit `config.py`:
```python
MARKET_PAIRS = [
    "YOUR_ASSET_1",
    "YOUR_ASSET_2",
    # Add more assets...
]
```

#### Strategy Parameters
Edit `config.py`:
```python
STRATEGY_CONFIG = {
    "name": "Three Black Crows",
    "timeframe": 60,  # 1 minute
    "safety_margin_percent": 0.15,
    "min_payout": 0.80
}
```

---

## 🌐 Deployment

### Local Deployment
1. Run `python main.py`
2. Open `INDEX.HTML` in browser
3. Access at `http://localhost:5000`

### Vercel Deployment (Frontend Only)
```bash
vercel --prod
```

**Note**: For full functionality on Vercel, you'll need to deploy the Python backend separately (e.g., on Heroku, Railway, or PythonAnywhere) and update the API endpoint in `INDEX.HTML`.

---

## 🛠️ Technologies Used

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Backend**: Python 3, Flask, Flask-CORS
- **Analysis**: Pandas, NumPy
- **Strategy**: Technical Analysis (RSI, SMA, Candlestick Patterns)
- **Design**: Custom CSS with animations, Font Awesome icons

---

## 📊 Performance

- **Signal Generation**: ~2 seconds per signal
- **Confidence Range**: 60-95%
- **Supported Assets**: 62+ pairs
- **Update Frequency**: 30-second intervals
- **Backend Response Time**: <100ms

---

## 🔒 Security

- **Password Protection**: Client-side authentication
- **No Data Collection**: All processing happens locally
- **HTTPS Ready**: Secure deployment on Vercel
- **XSS Protection**: Enabled via headers

---

## 📞 Support

- **Telegram Channel**: [@LUX_DOT](https://t.me/LUX_DOT)
- **Developer**: [@MAHIR_VIP](https://t.me/MAHIR_VIP)

---

## 📜 License

This project is for **educational and personal use only**. 

---

## ⚠️ Disclaimer

**IMPORTANT**: This tool is for educational purposes only. Binary options trading involves substantial risk of loss. Past performance does not guarantee future results. Always:

- Trade with money you can afford to lose
- Use proper risk management
- Test strategies on demo accounts first
- Consult with financial advisors
- Comply with local regulations

The developers are not responsible for any financial losses incurred through the use of this software.

---

## 🎯 Key Principles

1. **Safety First**: 15-20% safety margin on all trades
2. **One-Step MTG**: No martingale, fixed stakes
3. **AI-Driven**: Real technical analysis, not random signals
4. **Transparency**: Open-source strategy logic
5. **Education**: Learn while you trade

---

## 📚 Documentation

- [Three Black Crows Strategy Guide](THREE_BLACK_CROWS_STRATEGY.md)
- [API Documentation](main.py) - See inline comments
- [Configuration Guide](config.py) - Asset and strategy settings

---

## 🔄 Updates

### Latest Version: 2.0
- ✅ Python backend integration
- ✅ Real technical analysis (RSI, SMA)
- ✅ Three Black Crows pattern detection
- ✅ Confidence scoring system
- ✅ 62+ supported assets
- ✅ Premium UI redesign
- ✅ 30-second signal intervals

---

**Made with 💛 by MAHIR VIP**  
*One Step MTG - Premium Binary Signals*
