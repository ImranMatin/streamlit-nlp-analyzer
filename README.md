# 🧠 Streamlit NLP Analyzer

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

- You need **Python 3.x** installed on your system. Using a virtual environment (like Conda) is highly recommended.

### 1. Installation

- Clone the repository and install the required packages using the `requirements.txt` file:

## Clone the repository (Use your actual repo URL)
- git clone <YOUR_REPO_URL>
- cd streamlit-nlp-analyzer

## Install all necessary Python libraries
- pip install -r requirements.txt

### 2. Download NLTK Data
Two of the libraries (textblob and sumy) rely on linguistic data from NLTK. You must download these two specific files to run the app:

Bash

## Open the Python interpreter

Run these two lines inside the interpreter:

- import nltk
- nltk.download('punkt')
- nltk.download('punkt_tab')
- exit()

### 3. Run the Application

Start the Streamlit server from the root directory of the project:

- streamlit run app.py
- The application will automatically open in your web browser at http://localhost:8501.

### 🛠️ Tech Stack

- Framework: Streamlit

- Sentiment Analysis: TextBlob

- Summarization: Sumy (using LSA)

- Visualization: WordCloud and Matplotlib

streamlit-nlp-analyzer/ ├── app.py ├── .gitignore ├── requirements.txt ├── README.md └── LICENSE

### 🎉 Acknowledgements

- This project, Streamlit NLP Analyzer, was proudly developed and submitted as part of the **1M Celebration Hackathon**, **hosted by Tina   Huang**.

### 📄 License
- This project is licensed under the MIT License - see the LICENSE file for details.

⭐ If you found this project helpful, please give it a star on GitHub!


