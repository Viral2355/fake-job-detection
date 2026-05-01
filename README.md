
# 🧠 AI Cyber Job Fraud Detection System

## 🚀 Live Demo

https://fake-job-detection-eauxjcrn3mmayfumsheytz.streamlit.app/
---

## 📌 Overview

The **AI Cyber Job Fraud Detection System** is a machine learning-powered cybersecurity tool designed to identify fraudulent job postings in real-time.

This system analyzes job descriptions using **Natural Language Processing (NLP)** and classifies them as:

* ✅ Legitimate Job
* ❌ Fraudulent Job

It also provides:

* 📊 Confidence Score
* 🚨 Threat Level
* 🧠 Risk Indicators

---

## 🎯 Problem Statement

Online job platforms are increasingly targeted by scammers who post fake job listings to:

* Steal personal information
* Collect fraudulent registration fees
* Mislead job seekers

This project introduces an **AI-based detection layer** to prevent such fraud.

---

## ⚡ Key Features

* 🔍 Real-time job scanning
* 🧠 Machine Learning-based classification
* 📊 Confidence score output
* 🚨 Threat level detection (Low / Medium / High)
* 📉 Interactive analytics dashboard
* 🎨 Cybersecurity-themed UI (black + neon green)
* 💻 Terminal-style system logs

---

## 🏗️ Tech Stack

| Category      | Technology                  |
| ------------- | --------------------------- |
| Frontend      | Streamlit                   |
| Backend       | Python                      |
| ML Model      | Logistic Regression         |
| NLP           | TF-IDF Vectorization        |
| Libraries     | scikit-learn, pandas, numpy |
| Visualization | matplotlib, seaborn         |
| Deployment    | Streamlit Cloud             |

---

## 🧠 How It Works

1. User enters job description
2. Text is cleaned using NLP preprocessing
3. TF-IDF converts text into numerical features
4. Machine learning model predicts:

   * Real or Fake
   * Confidence score
5. System displays:

   * Threat level
   * Risk indicators
   * Visual analytics

---

## 📊 Model Performance

| Metric          | Value |
| --------------- | ----- |
| Accuracy        | 96%   |
| Fake Job Recall | 83%   |
| Precision       | 56%   |

> ⚠️ High recall is prioritized to ensure maximum fraud detection.

---

## 📁 Project Structure

```
fake-job-detection/
│
├── data/
├── model/
│   ├── model.pkl
│   └── vectorizer.pkl
├── utils/
│   └── preprocess.py
├── streamlit_app.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone  https://github.com/Viral2355/fake-job-detection.git
cd fake-job-detection
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Application

```bash
python -m streamlit run streamlit_app.py
```

---

## 🎥 Demo Usage

### 🔴 Fake Job Example

```
Earn $5000 weekly from home! No experience required. Pay a small fee to start.
```

### 🟢 Real Job Example

```
We are hiring a Software Developer with experience in Python and web development.
```

---

## 🧠 Key Insights

* Fraud detection prioritizes **recall over accuracy**
* Fake jobs often include:

  * “Earn money fast”
  * “No experience required”
  * “Registration fee”
* NLP helps detect hidden patterns in text

---

## 🌐 Future Enhancements

* 🔍 Real-time job scraping from portals
* 🧠 Explainable AI (SHAP integration)
* 📱 Mobile application
* 🔐 Integration with job platforms

---

## 🏆 Hackathon Value

This project is more than a classifier—it is a **cybersecurity solution** that:

* Protects users from job scams
* Improves trust in online hiring systems
* Demonstrates real-world AI application

---

## 👨‍💻 Author

**Viral Gujariya**
🔗 GitHub: https://github.com/Viral2355
🔗 LinkedIn: https://www.linkedin.com/in/viral-gujariya

---

## ⭐ Conclusion

This project showcases how **AI + cybersecurity principles** can be combined to build a real-world fraud detection system that protects users and enhances digital trust.

---
