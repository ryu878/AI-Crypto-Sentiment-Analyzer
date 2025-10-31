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

## 📞 Contact Me

I develop trading bots of any complexity, dashboards, and indicators for crypto exchanges, forex, and stocks. 🚀

To contact me, please send a message:

*   **Telegram:** [https://t.me/ryu8777](https://t.me/ryu8777) ✈️
*   **Discord:** [https://discord.gg/zSw58e9Uvf](https://discord.gg/zSw58e9Uvf) 🤝

***

## 🤝 Become My Crypto Partner

Start your trading journey on Bybit! Join using my referral link below:

**Join Bybit:** [https://www.bybit.com/invite?ref=P11NJW](https://www.bybit.com/invite?ref=P11NJW)

***

## 🖥️ VPS for Your Bots and Scripts

Keep your bots running 24/7! I prefer and recommend using **DigitalOcean**.

[![DigitalOcean Referral Badge](https://web-platforms.sfo2.digitaloceanspaces.com/WWW/Badge%202.svg)](https://www.digitalocean.com/?refcode=3d7f6e57bc04&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge)

**Get $200 in credit over 60 days** by using my referral link:

👉 [https://m.do.co/c/3d7f6e57bc04](https://m.do.co/c/3d7f6e57bc04)

