import streamlit as st
from model import predict_fake_news

# Page setup
st.set_page_config(page_title="AI Fake News Detector", page_icon="📰")

st.title("📰 AI Fake News Detector")
st.write("Paste a news headline or short article below, and AI will check its credibility.")

# User input
user_input = st.text_area("Enter news text here:", height=150)

if st.button("Check News"):
    if user_input.strip():
        with st.spinner("Analyzing..."):
            label, score = predict_fake_news(user_input)

        if label.lower() in ["fake", "false"]:
            st.error(f"❌ Likely Fake News ({score}% confidence)")
        else:
            st.success(f"✅ Likely True News ({score}% confidence)")

        st.caption("⚠️ This is an AI-based detector and should not be taken as absolute truth.")
    else:
        st.warning("Please enter some text to analyze.")
