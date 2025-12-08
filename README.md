
# 📊 YouTube Comment Insights (Data Engineering + NLP + Streamlit)

Analyze real-time YouTube comments to understand **audience mood**, **engagement patterns**, and **early video performance**.

This project builds an **end-to-end analytical pipeline** using YouTube Data API → Python → NLP → Streamlit dashboards.

---

## ▶ Live Demo

👉 Streamlit Cloud link coming after deployment

---

## 🚀 Key Features (MVP Version)

### ✔ Extract comments from any YouTube video

* Fetch comments through the official YouTube Data API
* No scraping (complies with YouTube policy)

### ✔ Sentiment Analysis

* NLTK VADER sentiment scoring
* Positive / Neutral / Negative classification
* Compound sentiment score

### ✔ Engagement Analytics (Initial Release)

* Most liked comment
* Top positive comments
* Top negative comments
* Sentiment distribution
* Engagement summary metrics

---

## 🧠 Insights Users Get

* Overall viewer mood (positive / negative / neutral)
* What people liked the most
* Strongest positive and negative reactions
* Sentiment histogram and keywords (coming soon)

This is useful for:

* YouTubers
* Marketers
* Content creators
* Influencers
* Businesses analyzing user reaction

---

## 🛠 Tech Stack

| Technology                   | Usage              |
| ---------------------------- | ------------------ |
| **Python**                   | core language      |
| **YouTube Data API**         | comment ingestion  |
| **Pandas**                   | data processing    |
| **NLTK (VADER)**             | sentiment analysis |
| **Seaborn / Matplotlib**     | visuals            |
| **Streamlit**                | dashboard UI       |
| **GitHub + Streamlit Cloud** | deployment         |

## 📦 Architecture (Phase 1 MVP)

YouTube URL →
  extract video ID →
    fetch comments →
      pandas processing →
        sentiment analysis (NLTK) →
          Streamlit dashboard

Upcoming:

Time-series analytics → engagement per day →
week-day analysis → early performance metrics

---

## 📌 Why this project?

I wanted a practical project showing:

* API ingestion
* Data engineering pipeline thinking
* Python NLP
* Real-time analytics
* Deployment skills
* Interactive dashboards
* User value (business insights)

This aligns directly with Data Engineer + ML Analyst roles.

---

## 🔥 Upcoming Additions (Roadmap)

### Phase 2 – Time & Engagement Analytics

* Comments per day visualization
* Weekday engagement graph
* First 1/3/5 day performance
* Upload performance insights

### Phase 3 – NLP Analytics

* Wordclouds
* Topic extraction
* Keyword sentiment
* Toxicity / Hate Speech detection

### Phase 4 – Dashboard Enhancements

* Filters
* Download report
* Multi-video comparison

### Phase 5 – Data Engineering

* Persist runs (SQL or MongoDB)
* Batch processing
* Async ingestion pipeline

---

## 🧑‍💻 Local Setup

git clone
cd youtube-insights
pip install -r requirements.txt
streamlit run app.py

Set your YouTube API key in `.env`:

YOUTUBE_API_KEY=YOUR_KEY_HERE

---

## 📢 Contact / Portfolio

* LinkedIn:
* Portfolio:
* GitHub:
