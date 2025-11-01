# Streamlit NLP Analyzer
Real-time AI tool for Sentiment Analysis, Summarization, and Word Clouds, built with Streamlit.


# 🧠 Streamlit NLP Analyzer

### FEAT: Implement core Streamlit NLP Analyzer (Hackathon Project)

This project is a powerful, real-time application built with Streamlit and Python for Natural Language Processing (NLP). It provides three core features for extracting value and insight from any block of text.

---

## 🌟 Key Features

* **1. Real-Time Sentiment Analysis:** Classifies text as **Positive 😊**, **Negative 😠**, or **Neutral 😐** using TextBlob.
    * Features a **Dynamic Threshold Slider** allowing users to adjust the model's sensitivity in real-time.
* **2. Text Summarization:** Generates a concise, extractive summary of long passages using the Sumy library (LSA algorithm).
* **3. Word Cloud Visualization:** Provides an instant, visual representation of the most frequent and important words in the input text.

---

## 🚀 Getting Started

Follow these steps to set up and run the application locally.

### Prerequisites

You need **Python 3.x** installed on your system. Using a virtual environment (like Conda) is highly recommended.

### 1. Installation

Clone the repository and install the required packages using the `requirements.txt` file:

```bash
# Clone the repository (Use your actual repo URL)
git clone <YOUR_REPO_URL>
cd streamlit-nlp-analyzer

# Install all necessary Python libraries
pip install -r requirements.txt

That's the perfect final step for your hackathon project! A well-structured README.md is crucial for presentation.

Here is the complete content for your README.md file, tailored for your Streamlit NLP Analyzer project.

📄 README.md for Streamlit NLP Analyzer
Markdown

# 🧠 Streamlit NLP Analyzer

### FEAT: Implement core Streamlit NLP Analyzer (Hackathon Project)

This project is a powerful, real-time application built with Streamlit and Python for Natural Language Processing (NLP). It provides three core features for extracting value and insight from any block of text.

---

## 🌟 Key Features

* **1. Real-Time Sentiment Analysis:** Classifies text as **Positive 😊**, **Negative 😠**, or **Neutral 😐** using TextBlob.
    * Features a **Dynamic Threshold Slider** allowing users to adjust the model's sensitivity in real-time.
* **2. Text Summarization:** Generates a concise, extractive summary of long passages using the Sumy library (LSA algorithm).
* **3. Word Cloud Visualization:** Provides an instant, visual representation of the most frequent and important words in the input text.

---

## 🚀 Getting Started

Follow these steps to set up and run the application locally.

### Prerequisites

You need **Python 3.x** installed on your system. Using a virtual environment (like Conda) is highly recommended.

### 1. Installation

Clone the repository and install the required packages using the `requirements.txt` file:

```bash
# Clone the repository (Use your actual repo URL)
git clone <YOUR_REPO_URL>
cd streamlit-nlp-analyzer

# Install all necessary Python libraries
pip install -r requirements.txt
2. Download NLTK Data
Two of the libraries (textblob and sumy) rely on linguistic data from NLTK. You must download these two specific files to run the app:

Bash

# Open the Python interpreter
python
Run these two lines inside the interpreter:

Python

import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
exit()
3. Run the Application
Start the Streamlit server from the root directory of the project:

Bash

streamlit run app.py
The application will automatically open in your web browser at http://localhost:8501.

🛠️ Tech Stack
Framework: Streamlit

Sentiment Analysis: TextBlob

Summarization: Sumy (using LSA)

Visualization: WordCloud and Matplotlib

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
