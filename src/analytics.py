import pandas as pd
from collections import Counter



def sentiment_counts(df: pd.DataFrame):
    return df["sentiment"].value_counts().to_dict()

def average_sentiment(df: pd.DataFrame):
    return df["compound"].mean()

def most_liked_comment(df: pd.DataFrame):
    return df.sort_values("like_count", ascending=False).iloc[0]

def top_positive(df: pd.DataFrame, n=3):
    return df[df["sentiment"] == "positive"].sort_values("compound", ascending=False).head(n)

def top_negative(df: pd.DataFrame, n=3):
    return df[df["sentiment"] == "negative"].sort_values("compound", ascending=True).head(n)

def comments_per_day(df: pd.DataFrame):
    return df.groupby("date").size().reset_index(name="comment_count")

def comments_by_weekday(df: pd.DataFrame):
    order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekday = df.groupby("weekday").size().reindex(order, fill_value=0)
    return weekday.reset_index(name="comment_count")

def early_performance(df: pd.DataFrame):
    """
    counts comments in first 1 / 3 / 5 days
    using first comment timestamp as video start
    """
    df = df.sort_values("published_at").copy()
    start = df["published_at"].min().normalize()
    df["days_since_start"] = (df["published_at"] - start).dt.days

    day1 = df[df["days_since_start"] <= 1].shape[0]
    day3 = df[df["days_since_start"] <= 3].shape[0]
    day5 = df[df["days_since_start"] <= 5].shape[0]

    return {
        "day1": day1,
        "day3": day3,
        "day5": day5,
    }


def top_words(df, sentiment, n=15):
    subset = df[df["sentiment"] == sentiment]
    all_words = [word for tokens in subset["tokens"] for word in tokens]
    return Counter(all_words).most_common(n)

def comments_by_hour(df: pd.DataFrame):
    return (
        df.groupby("hour")
          .size()
          .reset_index(name="comment_count")
          .sort_values("hour")
    )