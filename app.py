import gradio as gr
from scraper import fetch_coindesk_headlines
from sentiment import classify_sentiment
import pandas as pd
import matplotlib.pyplot as plt

def analyze():
    headlines = fetch_coindesk_headlines()
    results = []

    for line in headlines:
        sentiment, prob = classify_sentiment(line)
        results.append({"Headline": line, "Sentiment": sentiment, "Confidence": prob})

    df = pd.DataFrame(results)
    fig = plt.figure()
    df["Sentiment"].value_counts().plot(kind="bar", color=["red", "gray", "green"])
    plt.title("Sentiment Distribution")
    plt.xticks(rotation=0)
    plt.tight_layout()

    return df, fig

gr.Interface(
    fn=analyze,
    inputs=[],
    outputs=[gr.Dataframe(), gr.Plot()],
    title="📈 Crypto Sentiment Analyzer",
    description="Live headlines from CoinDesk analyzed by FinBERT."
).launch()
