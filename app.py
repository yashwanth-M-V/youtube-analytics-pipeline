import streamlit as st
from src.igestion import fetch_video_details, fetch_comments, extract_video_id
from src.processing import process_comments
from src.analytics import (
    sentiment_counts,
    average_sentiment,
    most_liked_comment,
    top_positive,
    top_negative,
    comments_per_day,
    comments_by_weekday,
    early_performance,
    top_words,
    comments_by_hour
)
from src.viz import (
    plot_sentiment_counts,
    plot_sentiment_histogram,
    plot_daily_comments,
    plot_weekday_comments,
    plot_sentiment_over_time,
    plot_sentiment_pie,
    plot_top_words,
    plot_hourly_comments
)

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="YouTube Insights Dashboard",
    layout="wide"
)

st.title("📊 YouTube Insights Dashboard")
st.write("NOTE: Only Initial 500 comments analyzed for sentiment & engagement.")
st.write("🚀 Paste a YouTube URL below to analyze audience sentiment & engagement.")

# ------------------ URL INPUT ------------------
url = st.text_input("🎬 YouTube URL", key="main_url_input")

# If URL provided
if url:
    video_id = extract_video_id(url)
    video_info = fetch_video_details(video_id)

    if video_info:
        # ------------------ TOP GRID ------------------
        thumbnail_url = f"https://img.youtube.com/vi/{video_id}/0.jpg"

        col_img, col_info = st.columns([3,7])

        # LEFT - Thumbnail
        with col_img:
            st.image(thumbnail_url, width=300)

        # right - Title + Channel + Published + Fetch Button
        with col_info:
            st.subheader("🎬 " + video_info["title"])
            st.write(f"**Channel:** {video_info['channel']}")
            st.caption(f"📅 Published on: {video_info['published'][:10]}")
            st.write("")  # spacer
            fetch_clicked = st.button("📥 Fetch Comments")

        # ------------------ AFTER CLICK ------------------
        if fetch_clicked:
            with st.spinner("Fetching comments & running analysis..."):
                df = process_comments(fetch_comments(video_id, max_comments=500))

            st.success(f"Fetched {len(df)} comments successfully!")
            st.write(df.head())

            # ----- Analytics -----
            counts = sentiment_counts(df)
            avg = average_sentiment(df)
            most = most_liked_comment(df)
            top_pos = top_positive(df)
            top_neg = top_negative(df)
            daily = comments_per_day(df)
            weekday = comments_by_weekday(df)
            early = early_performance(df)
            top_words(df, "positive")
            top_words(df, "negative")
            hourly = comments_by_hour(df)

            # ------------------ Metrics ------------------
            st.subheader("📈 Sentiment Summary")

            col1, col2, col3 = st.columns(3)
            col1.metric("Positive", counts.get("positive", 0))
            col2.metric("Neutral", counts.get("neutral", 0))
            col3.metric("Negative", counts.get("negative", 0))

            col4, col5, col6 = st.columns(3)
            col4.metric("Avg Compound", round(avg, 3))
            col5.metric("Day 1", early["day1"])
            col6.metric("Day 3", early["day3"])

            col7, _ = st.columns([1, 2])
            col7.metric("Day 5", early["day5"])

            # ------------------ Most Liked ------------------
            st.subheader("🏆 Most Liked Comment")
            st.write(most["author"])
            st.write(most["text"])
            st.write("👍 Likes:", most["like_count"])

            # ------------------ Charts ------------------
            st.subheader("📊 Sentiment Distribution")
            st.pyplot(plot_sentiment_counts(df), use_container_width=False)

            st.subheader("📊 Sentiment Histogram")
            st.pyplot(plot_sentiment_histogram(df), use_container_width=False)

            st.subheader("📈 Comments per Day")
            st.pyplot(plot_daily_comments(daily), use_container_width=False)

            st.subheader("🗓 Comments by Weekday")
            st.pyplot(plot_weekday_comments(weekday), use_container_width=False)

            st.subheader("📉 Sentiment Trend Over Time")
            st.pyplot(plot_sentiment_over_time(df), use_container_width=False)
            
            st.subheader("🟢 Sentiment Breakdown")
            pie_fig = plot_sentiment_pie(df)
            st.plotly_chart(pie_fig, use_container_width=False)


            top_pos_words = top_words(df, "positive", 15)
            top_neg_words = top_words(df, "negative", 15)

            st.subheader("🔠 Top Positive Words")
            st.pyplot(plot_top_words(top_pos_words, "Positive Words"), use_container_width=False)

            st.subheader("🔡 Top Negative Words")
            st.pyplot(plot_top_words(top_neg_words, "Negative Words"), use_container_width=False)
            
            st.subheader("🕒 Comments by Hour")
            st.pyplot(plot_hourly_comments(hourly), use_container_width=False)