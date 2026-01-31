import streamlit as st
from sentiment_analysis import analyze_sentiment
from data_processing import clean_text

st.title("Sentiment Analysis Web App")

user_input = st.text_area("Enter text")

if st.button("Analyze"):
    if user_input.strip():
        cleaned_text = clean_text(user_input)
        scores = analyze_sentiment(cleaned_text)
        st.write("Sentiment Scores:", scores)
    else:
        st.warning("Please enter some text")
