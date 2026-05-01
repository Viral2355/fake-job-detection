import os
import joblib
from utils.preprocess import clean_text

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = joblib.load(os.path.join(BASE_DIR, 'model', 'model.pkl'))
vectorizer = joblib.load(os.path.join(BASE_DIR, 'model', 'vectorizer.pkl'))

def predict_job(text):
    text = clean_text(text)
    vec = vectorizer.transform([text])
    pred = model.predict(vec)[0]

    return "Fake Job ❌" if pred == 1 else "Real Job ✅"


if __name__ == "__main__":
    text = input("Enter job description:\n")
    print(predict_job(text))