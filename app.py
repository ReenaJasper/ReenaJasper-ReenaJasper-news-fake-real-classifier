import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load('news_classifier_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

st.title("📰 News Article Classifier")
st.subheader("Check if a news article is Real or Fake")

# Input text
user_input = st.text_area("Enter the news content:", height=200)

# Predict button
if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        input_vector = vectorizer.transform([user_input])
        prediction = model.predict(input_vector)[0]
        result = "🟢 Real News" if prediction == 1 else "🔴 Fake News"
        st.success(f"Prediction: **{result}**")
