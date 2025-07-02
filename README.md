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

## Contacts
To contact me please pm:

Telegram: https://t.me/ryu8777

Discord: https://discord.gg/zSw58e9Uvf
