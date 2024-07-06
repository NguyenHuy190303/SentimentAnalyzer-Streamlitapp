import streamlit as st
from textblob import TextBlob

# Title of the application
st.title("Sentiment Analysis App")

# Input text box
user_input = st.text_area("Enter Text:")

# When the button is clicked
if st.button("Analyze"):
    if user_input:
        # Analyzing the sentiment of the input text
        blob = TextBlob(user_input)
        sentiment = blob.sentiment

        # Displaying the results
        st.write("Sentiment Polarity: ", sentiment.polarity)
        st.write("Sentiment Subjectivity: ", sentiment.subjectivity)

        if sentiment.polarity > 0:
            st.write("Overall Sentiment: Positive")
        elif sentiment.polarity < 0:
            st.write("Overall Sentiment: Negative")
        else:
            st.write("Overall Sentiment: Neutral")
    else:
        st.write("Please enter some text to analyze.")
