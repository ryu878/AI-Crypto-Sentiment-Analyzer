from transformers import BertTokenizer, BertForSequenceClassification
import torch
import torch.nn.functional as F

# Load model and tokenizer
MODEL_NAME = "yiyanghkust/finbert-tone"
tokenizer = BertTokenizer.from_pretrained(MODEL_NAME)
model = BertForSequenceClassification.from_pretrained(MODEL_NAME)

def classify_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = F.softmax(outputs.logits, dim=1)
        sentiment = torch.argmax(probs, dim=1).item()

    labels = {0: "negative", 1: "neutral", 2: "positive"}
    return labels[sentiment], round(probs[0][sentiment].item(), 3)
