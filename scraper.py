import requests
from bs4 import BeautifulSoup

def fetch_coindesk_headlines():
    url = "https://www.coindesk.com/"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")

    headlines = []
    for tag in soup.select("a.card-title"):
        title = tag.get_text(strip=True)
        if title:
            headlines.append(title)

    return headlines[:10]  # limit to top 10 for demo
