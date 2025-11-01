# 1. Import Libraries
import streamlit as st
from textblob import TextBlob
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
# >> NEW IMPORTS: for Word Cloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 2. Define the Main Analysis Function (Unchanged)


def analyze_sentiment(text, threshold):
    """
    Performs sentiment analysis using TextBlob and returns the result.
    """
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > threshold:
        sentiment = "Positive 😊"
        color = "green"
    elif polarity < -threshold:
        sentiment = "Negative 😠"
        color = "red"
    else:
        sentiment = "Neutral 😐"
        color = "gray"

    return sentiment, polarity, color

# 3. Define the Summarization Function (Unchanged)


def summarize_text(text, sentences_count=3):
    """
    Generates a summary of the text using the Sumy library (LSA Summarizer).
    """
    try:
        if len(text.split()) < 30:
            return "Text is too short for meaningful summarization (min 30 words recommended)."

        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary_sentences = summarizer(parser.document, sentences_count)

        summary = " ".join(str(s) for s in summary_sentences)

        return summary
    except Exception as e:
        # This catches the NLTK error if data is missing, providing a friendly message
        return "NLTK data is missing for summarization. Please run the NLTK download fix."

# >> NEW FUNCTION: Word Cloud Generation


def create_word_cloud(text):
    """
    Generates a Word Cloud from the input text.
    """
    # Create and generate a word cloud image:
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        max_words=100,
        colormap='viridis'  # Choose a color scheme
    ).generate(text)

    # Display the generated image in Streamlit
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)


# 4. Configure the Streamlit App Interface
st.set_page_config(
    page_title="Sensum AI: Real-Time Analyzer",
    layout="centered"
)

# App Header
st.title("🧠 Sensum AI: Real-Time Sentiment Analyzer")
st.markdown("---")

# Description
st.write(
    """
    Your powerful tool for **Sentiment Analysis**, **Text Summarization**, and **Visual Tagging** (Word Cloud).
    """
)

# 5. Add the Dynamic Threshold Slider (Unchanged)
st.subheader("Model Configuration (Sentiment)")
threshold = st.slider(
    "**Sensitivity Threshold (Polarity)**",
    min_value=0.0,
    max_value=0.5,
    value=0.1,
    step=0.05,
    help="Higher values make the model LESS sensitive."
)
st.markdown(f"Current Threshold: **$\pm {threshold}$**")
st.markdown("---")

# 6. Create the Input Field
user_input = st.text_area(
    "**Paste your text here:**",
    value="",
    height=200,
    placeholder="Paste a long paragraph, article, or review for analysis and visualization."
)

# 7. Handle Analysis Buttons (Updated to include Word Cloud)
col1, col2, col3 = st.columns(3)

# Sentiment Button
with col1:
    if st.button("**Analyze Sentiment**", use_container_width=True):
        if user_input:
            sentiment, polarity, color = analyze_sentiment(
                user_input, threshold)

            st.subheader("Sentiment Result:")
            st.markdown(
                f'<div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; border-left: 5px solid {color};">'
                f'<h2>Sentiment: <span style="color: {color};">{sentiment}</span></h2>'
                f'<p>Polarity Score: <strong>{polarity:.4f}</strong> (Neutral range is $\pm {threshold}$)</p>'
                '</div>',
                unsafe_allow_html=True
            )
        else:
            st.warning("Please enter some text to analyze.")

# Summarization Button
with col2:
    if st.button("**Generate Summary**", use_container_width=True):
        if user_input:
            summary = summarize_text(user_input, sentences_count=3)

            st.subheader("Summary Result:")
            st.info(summary)

            original_word_count = len(user_input.split())
            summary_word_count = len(summary.split()) if summary else 0
            st.caption(
                f"Original Words: {original_word_count} | Summary Words: {summary_word_count}")
        else:
            st.warning("Please enter some text to summarize.")

# Word Cloud Button (NEW!)
with col3:
    if st.button("**Generate Word Cloud**", use_container_width=True):
        if user_input:
            st.subheader("Word Cloud Visualization:")
            create_word_cloud(user_input)
            st.caption("Larger words appear more frequently in the text.")
        else:
            st.warning("Please enter some text to generate the word cloud.")


# 8. Project Footer
st.markdown("---")
st.caption(
    "Hackathon Project powered by Streamlit, TextBlob, Sumy, and Matplotlib.")
