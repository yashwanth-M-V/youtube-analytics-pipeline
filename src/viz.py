import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.express as px

plt.rcParams.update({
    "font.size": 6,
    "axes.titlesize": 6,
    "axes.labelsize": 5,
    "xtick.labelsize":5,
    "ytick.labelsize": 5,
})

def plot_sentiment_counts(df):
    fig, ax = plt.subplots(figsize=(2,2))
    sns.countplot(x="sentiment", data=df, ax=ax)
    ax.set_title("Sentiment Distribution")
    plt.tight_layout()
    return fig


def plot_sentiment_histogram(df):
    fig, ax = plt.subplots(figsize=(2,2))
    sns.histplot(df["compound"], bins=20, ax=ax)
    ax.set_title("Sentiment Score Histogram")
    plt.tight_layout()
    return fig


def plot_daily_comments(daily_df):
    fig, ax = plt.subplots(figsize=(2,2))
    sns.lineplot(data=daily_df, x="date", y="comment_count", ax=ax)
    ax.set_title("Comments per Day")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig


def plot_weekday_comments(weekday_df):
    fig, ax = plt.subplots(figsize=(2,2))
    sns.barplot(data=weekday_df, x="weekday", y="comment_count", ax=ax)
    ax.set_title("Comments by Weekday")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig


def plot_sentiment_over_time(df):
    df = df.sort_values("published_at").copy()
    df["rolling_mean"] = df["compound"].rolling(window=20, min_periods=5).mean()

    fig, ax = plt.subplots(figsize=(2,2))
    ax.plot(df["published_at"], df["rolling_mean"])
    ax.set_title("Rolling Sentiment Over Time")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig

def plot_sentiment_pie(df):
    fig = px.pie(
        names=df["sentiment"],
        title="Sentiment Percentage",
        hole=0.4,                # donut look
    )
    return fig

def plot_top_words(words, title):
    words, counts = zip(*words)
    fig, ax = plt.subplots(figsize=(3,2))
    sns.barplot(x=list(counts), y=list(words), ax=ax)
    ax.set_title(title)
    plt.tight_layout()
    return fig

def plot_hourly_comments(hourly_df):
    fig, ax = plt.subplots(figsize=(3,2))
    sns.barplot(data=hourly_df, x="hour", y="comment_count", ax=ax)
    ax.set_title("Comments by Hour of Day")
    plt.tight_layout()
    return fig