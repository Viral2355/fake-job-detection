import streamlit as st
import os, time, joblib, numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from utils.preprocess import clean_text

# -------------------------
# CONFIG
# -------------------------
st.set_page_config(page_title="Cyber AI Job Detector", layout="wide")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, 'model/model.pkl'))
vectorizer = joblib.load(os.path.join(BASE_DIR, 'model/vectorizer.pkl'))

# -------------------------
# 🎨 CYBER STYLE (STRONG OVERRIDE)
# -------------------------
st.markdown("""
<style>

/* GLOBAL */
html, body, [class*="css"] {
    background-color: #050a08 !important;
    color: #00ff9f !important;
}

/* SYSTEM STATUS */
.status {
    font-size:14px;
    color:#00ff9f;
    margin-bottom:10px;
}

/* HERO */
.hero {
    background: linear-gradient(90deg,#001a14,#003d2f);
    padding: 25px;
    border-radius: 12px;
    border: 1px solid #00ff9f;
    text-align: center;
    animation: glow 2s infinite;
}

/* GLOW EFFECT */
@keyframes glow {
    0% { box-shadow: 0 0 5px #00ff9f; }
    50% { box-shadow: 0 0 20px #00ff9f; }
    100% { box-shadow: 0 0 5px #00ff9f; }
}

/* CARD */
.card {
    background: #0b1310;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #00ff9f33;
    transition: 0.3s;
}

.card:hover {
    box-shadow: 0 0 15px #00ff9f;
}

/* TEXTAREA */
textarea {
    background-color: #000 !important;
    color: #00ff9f !important;
    border: 1px solid #00ff9f !important;
}

/* BUTTON */
button {
    background: #00ff9f !important;
    color: black !important;
    border-radius: 8px !important;
    font-weight: bold !important;
}

/* PROGRESS */
div[data-testid="stProgressBar"] > div > div {
    background: #00ff9f !important;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #000 !important;
}

/* METRICS */
[data-testid="stMetricValue"] {
    color: #00ff9f !important;
    font-size: 26px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# SYSTEM STATUS
# -------------------------
st.markdown("<div class='status'>🟢 System Online | 🔒 Security Active | ⚡ AI Running</div>", unsafe_allow_html=True)

# -------------------------
# HERO
# -------------------------
st.markdown("""
<div class='hero'>
    <h1>🧠 CYBER JOB FRAUD DETECTOR</h1>
    <p>Real-time AI Threat Detection System</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# -------------------------
# LAYOUT
# -------------------------
col1, col2 = st.columns([1.3, 1])

# INPUT
with col1:
    st.markdown("<div class='card'><h3>📄 Job Input</h3></div>", unsafe_allow_html=True)
    user_input = st.text_area("Paste job description...", height=220)
    analyze = st.button("⚡ Scan Job")

# RESULT
with col2:
    st.markdown("<div class='card'><h3>📊 Scan Result</h3></div>", unsafe_allow_html=True)

    if analyze and user_input:

        with st.spinner("🔍 Deep scanning..."):
            time.sleep(1.5)

        cleaned = clean_text(user_input)
        vec = vectorizer.transform([cleaned])

        prob = model.predict_proba(vec)[0]
        pred = model.predict(vec)[0]

        # RESULT
        if pred == 1:
            st.error("🚨 THREAT DETECTED")
            confidence = prob[1]
        else:
            st.success("✅ SYSTEM SAFE")
            confidence = prob[0]

        st.metric("Confidence", f"{confidence*100:.2f}%")

        # THREAT LEVEL
        if prob[1] > 0.7:
            st.error("Threat Level: HIGH 🔴")
        elif prob[1] > 0.4:
            st.warning("Threat Level: MEDIUM 🟡")
        else:
            st.success("Threat Level: LOW 🟢")

        # PROBABILITY
        st.write("### 📊 Probability")
        st.progress(int(prob[1]*100))
        st.caption(f"Fake: {prob[1]*100:.2f}%")

        st.progress(int(prob[0]*100))
        st.caption(f"Real: {prob[0]*100:.2f}%")

        # KEYWORDS
        st.write("### 🧠 Risk Indicators")
        keywords = ["earn", "money", "quick", "fee", "urgent"]
        found = [w for w in keywords if w in user_input.lower()]

        if found:
            st.warning("⚠️ Suspicious: " + ", ".join(found))
        else:
            st.success("No major risk signals")

# -------------------------
# ANALYTICS
# -------------------------
st.write("")
st.markdown("<div class='card'><h3>📉 Model Analytics</h3></div>", unsafe_allow_html=True)

cm = np.array([[3291, 112],
               [30, 143]])

fig, ax = plt.subplots(figsize=(4,3))
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', cbar=False)
plt.xlabel("Predicted")
plt.ylabel("Actual")

st.pyplot(fig)

col1, col2, col3 = st.columns(3)
col1.metric("Accuracy", "96%")
col2.metric("Fake Recall", "83%")
col3.metric("Precision", "56%")