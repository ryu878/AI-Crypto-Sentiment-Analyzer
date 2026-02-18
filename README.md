# AI Crypto Sentiment Analyzer
Scrapes recent crypto headlines or tweets and uses AI to classify sentiment: bullish, bearish, or neutral.
It pulls recent news or tweets and uses a Transformer-based model (like FinBERT) to classify the sentiment as 🟢 bullish, 🔴 bearish, or ⚪ neutral.

### 🔧 Features
- 📰 Scrapes news from CoinDesk, CoinTelegraph, or Twitter (X)

- 🧠 Uses FinBERT or custom-trained BERT for financial sentiment

- 🟢 Classifies sentiment per article/tweet

- 📊 Summary chart of results

- 💻 Local Python app, no need for cloud APIs

  

### 📦 Installation

```
git clone https://github.com/ryu878/AI-Crypto-Sentiment-Analyzer.git
cd AI-Crypto-Sentiment-Analyzer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### ▶️ Run the App
```
python app.py
```
Then go to http://localhost:7860 in your browser.

### 📁 Project Structure

```
📦 AI-Crypto-Sentiment-Analyzer/
├── app.py               # Gradio interface
├── sentiment.py         # Sentiment classification logic
├── scraper.py           # News scraping functions
├── requirements.txt     # Python dependencies
└── README.md
```

### 🧠 Models Used
- yiyanghkust/finbert-tone

- HuggingFace Transformers + PyTorch

- Gradio for UI

### ✅ Future Ideas
- Add Twitter/X scraping via Tweepy

- Include multiple news sources

- Export data to CSV

- Telegram bot interface


***

## 📄 License
MIT License - Feel free to modify and distribute.


## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check issues page.

## ⚠️ Disclaimer

> This project is for informational and educational purposes only. You should not use this information or any other material as legal, tax, investment, financial, or other advice. Nothing contained here is a recommendation, endorsement, or offer by me to buy or sell any securities or other financial instruments.
>
> **If you intend to use real money, use it at your own risk.**
>
> Under no circumstances will I be responsible or liable for any claims, damages, losses, expenses, costs, or liabilities of any kind, including but not limited to direct or indirect damages for loss of profits.

***

## 📌 Quantitative Researcher | Algorithmic Trader | Trading Systems Architect

Quantitative researcher and trading systems engineer with end-to-end ownership of systematic strategies — from research and statistical validation to low-latency execution and production deployment.

Core focus areas:
- Systematic strategy design and validation
- Market microstructure analysis (order book dynamics, liquidations, volume, delta, liquidity, spread behavior, funding)
- Backtesting framework development (tick-level and historical data)
- Execution engine architecture and order lifecycle management
- Real-time market data processing
- Risk-aware system design
- Production-grade trading infrastructure (24/7 environments)

Experience across crypto (CEX, DEX), FX, and exchange-traded markets.

## Technical Stack

- Languages: Python, C++, MQL5
- Execution & Connectivity: REST, WebSocket, FIX
- Infrastructure: Linux, Docker, Redis, PostgreSQL, ClickHouse
- Analytics: NumPy, Pandas, custom backtesting frameworks

## Contact

Email: ryu8777@gmail.com

***
