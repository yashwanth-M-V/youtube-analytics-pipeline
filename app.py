import streamlit as st
from src.igestion import extract_video_id, fetch_comments
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
)   

st.title("YouTube Insights Dashboard")
st.write("🚀 Ready to analyze a YouTube video!")


from src.igestion import extract_video_id

url = st.text_input("YouTube URL", key="main_url_input")


if url:
    video_id = extract_video_id(url)
    st.write("Video ID:", video_id)

    if st.button("Fetch Comments"):
        with st.spinner("Fetching comments..."):
            df = process_comments(fetch_comments(video_id, max_comments=200))

        st.write(df.head(50))
        st.write("Total comments fetched:", len(df))
    
        st.subheader("Sentiment Analysis")
        counts = sentiment_counts(df)
        avg = average_sentiment(df)
        most = most_liked_comment(df)
        top_pos = top_positive(df)
        top_neg = top_negative(df)
        daily = comments_per_day(df)
        weekday = comments_by_weekday(df)
        early = early_performance(df)

        st.write("Sentiment counts:", counts)
        st.write("Average sentiment:", avg)
        st.write("Most liked comment:", most)
        st.write("Top positive:", top_pos)
        st.write("Top negative:", top_neg)
        st.write("Daily counts:", daily)
        st.write("Weekday counts:", weekday)
        st.write("Early performance:", early)
