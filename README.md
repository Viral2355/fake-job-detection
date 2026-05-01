
#  AI Cyber Job Fraud Detection System

##  Overview

The **AI Cyber Job Fraud Detection System** is a machine learning-powered platform designed to identify fraudulent job postings in real-time.  

It analyzes job descriptions using Natural Language Processing (NLP) techniques and classifies them as **Real** or **Fake** with confidence scores and threat levels.

---

##  Problem Statement

Online job platforms are increasingly targeted by scammers who post fake job listings to:
- Steal personal data
- Collect fraudulent fees
- Mislead job seekers

This project provides a **cyber-security inspired solution** to detect such threats automatically.

---

##  Features

-  Real-time job analysis  
-  AI-based fraud detection (ML model)  
-  Confidence score prediction  
-  Threat level detection (Low / Medium / High)  
-  Model performance dashboard  
-  Cyber-style interactive UI (Streamlit)  

---

##  Tech Stack

- **Frontend/UI:** Streamlit  
- **Backend:** Python  
- **Machine Learning:** Scikit-learn  
- **NLP:** TF-IDF Vectorization  
- **Model:** Logistic Regression  
- **Visualization:** Matplotlib, Seaborn  

---

##  Model Performance

| Metric | Score |
|------|------|
| Accuracy | 96% |
| Fake Job Recall | 83% |
| Precision | 56% |

> High recall ensures maximum detection of fraudulent jobs, which is critical for safety.

---

## How It Works

1. User enters job description  
2. Text is preprocessed (cleaning, stopwords removal)  
3. TF-IDF converts text into numerical features  
4. ML model predicts:
   - Real or Fake  
   - Confidence score  
5. System displays:
   - Threat level  
   - Risk indicators  

---

## Installation & Setup

### Step 1: Clone Repository
```bash
git clone <your-repo-link>
cd fake-job-detection
=======
# fake-job-detection
