# 🛡️ AI Scam & Fraud Message Detector

An AI-powered web application that detects whether a message is likely to be a **scam/fraud** or **safe**.

The project uses **Natural Language Processing (NLP)** and **Machine Learning** to analyze the text and identify suspicious patterns.

---

## 🎯 Objective

The main objective of this project is to help users identify potentially fraudulent messages before they click suspicious links, share personal information, or make payments.

---

## ✨ Features

- 🔍 Detects potentially fraudulent messages
- 🚨 Classifies messages as **Scam** or **Safe**
- 📊 Displays prediction probability
- 🚩 Identifies common scam red flags
- 🛡️ Provides safety recommendations
- 📱 Simple and user-friendly Streamlit interface
- 🤖 Uses Machine Learning for message classification
- ⚡ Runs locally without requiring an external AI API

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Streamlit | Web application interface |
| Pandas | Dataset handling |
| NumPy | Numerical operations |
| Scikit-learn | Machine Learning |
| TF-IDF | Text feature extraction |
| Logistic Regression | Message classification |
| Joblib | Saving and loading the trained model |
| python-dotenv | Environment variable management |

---

## 🧠 Machine Learning Model

The project uses a combination of:

### TF-IDF

**TF-IDF (Term Frequency-Inverse Document Frequency)** converts text messages into numerical features that the machine learning model can understand.

### Logistic Regression

Logistic Regression is used to classify the message into two categories:

- `scam`
- `safe`

The trained model is saved as:

```text
scam_detector_model.pkl