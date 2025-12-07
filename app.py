import streamlit as st
from src.igestion import extract_video_id, fetch_comments
from src.processing import process_comments

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
    