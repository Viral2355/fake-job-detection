import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

from utils.preprocess import clean_text

# 📁 Correct path handling
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(BASE_DIR, 'data', 'fake_job_postings.csv')

# Load dataset
df = pd.read_csv(data_path)
df.fillna('', inplace=True)

# Combine text columns
df['text'] = df['title'] + " " + df['description'] + " " + df['requirements']

# Clean text
df['text'] = df['text'].apply(clean_text)

# Features & labels
X = df['text']
y = df['fraudulent']

print("📊 Class Distribution:")
print(y.value_counts())

# TF-IDF with bigrams
vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1,2))
X_vec = vectorizer.fit_transform(X)

# Train-test split (IMPORTANT)
X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.2, random_state=42, stratify=y
)

# Model with class balancing
model = LogisticRegression(class_weight='balanced', max_iter=1000)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
print("\n📊 Classification Report:\n")
print(classification_report(y_test, y_pred))

print("\n📊 Confusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))

# Save model
model_path = os.path.join(BASE_DIR, 'model', 'model.pkl')
vectorizer_path = os.path.join(BASE_DIR, 'model', 'vectorizer.pkl')

joblib.dump(model, model_path)
joblib.dump(vectorizer, vectorizer_path)

print("\n✅ Model trained and saved successfully!")