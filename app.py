import streamlit as st
from transformers import pipeline

# Title
st.title("AI Notes Generator 📘✨")

st.write("Paste any text below, and get AI-generated summarized notes!")

# Input text
text = st.text_area("Enter your text here:")

# Load summarizer
@st.cache_resource
def load_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_model()

# Button
if st.button("Generate Notes"):
    if text.strip() == "":
        st.warning("⚠️ Please enter some text first!")
    else:
        with st.spinner("Generating notes... ⏳"):
            summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
            st.success("✅ Here are your AI-generated notes:")
            st.write(summary[0]['summary_text'])
