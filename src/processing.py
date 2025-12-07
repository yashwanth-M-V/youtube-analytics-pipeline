import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import re
from nltk.corpus import stopwords
STOPWORDS = set(stopwords.words("english"))


sia = SentimentIntensityAnalyzer()

def clean_text(text):
    return str(text).replace("\n", " ").strip()

def add_sentiment(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # clean text
    df["clean_text"] = df["text"].apply(clean_text)

    # compound score
    df["compound"] = df["clean_text"].apply(
        lambda t: sia.polarity_scores(t)["compound"]
    )

    # label sentiment
    def label(score):
        if score >= 0.05:
            return "positive"
        elif score <= -0.05:
            return "negative"
        else:
            return "neutral"

    df["sentiment"] = df["compound"].apply(label)
    return df

def add_time_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["date"] = df["published_at"].dt.date
    df["weekday"] = df["published_at"].dt.day_name()
    df["hour"] = df["published_at"].dt.hour
    return df

def process_comments(df: pd.DataFrame) -> pd.DataFrame:
    df = add_sentiment(df)
    df = add_time_features(df)
    df["tokens"] = df["clean_text"].apply(tokenize)
    return df


def tokenize(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    words = text.split()
    return [w for w in words if w not in STOPWORDS and len(w) > 2]