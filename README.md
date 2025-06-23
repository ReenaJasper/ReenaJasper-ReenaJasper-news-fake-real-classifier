 News Article Classification – Fake vs Real

This project uses Natural Language Processing (NLP) and Machine Learning to classify news articles as **Fake** or **Real**.
Objective: To build a classification model that detects fake news based on article content using traditional ML techniques and deploy it via Streamlit.
Live Demo: https://reenajasper-reenajasper-news-fake-real-classifier-dmn9mx3wgjsa.streamlit.app/  
Tools & Technologies used:
- Python
- Pandas, NumPy
- Scikit-learn
- NLTK
- Streamlit
- TF-IDF Vectorizer
- Logistic Regression

 Files in This Repo
| File | Description |
|------|-------------|
| `app.py` | Streamlit app for prediction |
| `news_classifier_model.pkl` | Trained logistic regression model |
| `tfidf_vectorizer.pkl` | TF-IDF vectorizer |
| `requirements.txt` | Python dependencies |
| `notebook.ipynb` | (Optional) Training notebook if added |


Model Overview
- Vectorizer: TF-IDF with top 5000 features
- Classifier: Logistic Regression
- Accuracy: ~99% on test data

📈 How It Works
1. User enters news content.
2. Text is cleaned & transformed using TF-IDF.
3. Model predicts: 🟢 Real or 🔴 Fake.
4. Result is displayed in a clean interface.

✅ Deliverables
- Jupyter Notebook (Colab)
- Trained model + vectorizer
- Streamlit Web App
- 2-page Report (see below)

