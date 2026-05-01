import os
from flask import Flask, request, render_template_string
import joblib
from utils.preprocess import clean_text

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = joblib.load(os.path.join(BASE_DIR, 'model', 'model.pkl'))
vectorizer = joblib.load(os.path.join(BASE_DIR, 'model', 'vectorizer.pkl'))

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Fake Job Detector</title>
<style>
body {
    font-family: Arial;
    background: linear-gradient(to right, #1e3c72, #2a5298);
    color: white;
    text-align: center;
    padding: 40px;
}

.container {
    background: white;
    color: black;
    padding: 30px;
    border-radius: 15px;
    width: 60%;
    margin: auto;
    box-shadow: 0 0 20px rgba(0,0,0,0.2);
}

textarea {
    width: 90%;
    height: 150px;
    padding: 10px;
    border-radius: 10px;
    border: 1px solid #ccc;
    font-size: 14px;
}

button {
    margin-top: 15px;
    padding: 10px 25px;
    border: none;
    border-radius: 8px;
    background: #2a5298;
    color: white;
    font-size: 16px;
    cursor: pointer;
}

button:hover {
    background: #1e3c72;
}

.result {
    margin-top: 20px;
    padding: 15px;
    border-radius: 10px;
    font-size: 18px;
}

.real {
    background: #d4edda;
    color: #155724;
}

.fake {
    background: #f8d7da;
    color: #721c24;
}
</style>
</head>

<body>

<h1>🚀 Fake Job Detection System</h1>

<div class="container">
<form method="POST">
<textarea name="text" placeholder="Paste job description here..."></textarea><br>
<button type="submit">Check Job</button>
</form>

{% if result %}
<div class="result {{ label_class }}">
    <strong>{{ result }}</strong><br>
    Confidence: {{ confidence }}%
</div>
{% endif %}

</div>

</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    confidence = None
    label_class = ""

    if request.method == 'POST':
        text = request.form['text']
        cleaned = clean_text(text)
        vec = vectorizer.transform([cleaned])

        prob = model.predict_proba(vec)[0]
        pred = model.predict(vec)[0]

        if pred == 1:
            result = "❌ Fake Job Detected"
            confidence = round(prob[1] * 100, 2)
            label_class = "fake"
        else:
            result = "✅ Real Job Detected"
            confidence = round(prob[0] * 100, 2)
            label_class = "real"

    return render_template_string(HTML, result=result, confidence=confidence, label_class=label_class)

if __name__ == "__main__":
    app.run(debug=True)