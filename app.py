#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import joblib
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer

# Load the saved model and vectorizer
model_filename = 'review_analysis_model.joblib'
vectorizer_filename = 'review_analysis_vectorizer.joblib'
loaded_classifier = joblib.load(model_filename)
loaded_vectorizer = joblib.load(vectorizer_filename)

# Function to preprocess the input text
def preprocess_text(text):
    return loaded_vectorizer.transform([text])

# Function to predict the sentiment label
def predict_sentiment(text):
    preprocessed_text = preprocess_text(text)
    prediction = loaded_classifier.predict(preprocessed_text)[0]
    return prediction

# Set up the Streamlit app
st.title("IMDb Sentiment Analysis")
text_input = st.text_area("Enter your review:")
prediction_button = st.button("Predict Sentiment")

# Perform prediction when the button is clicked
if prediction_button:
    if text_input:
        prediction = predict_sentiment(text_input)
        st.write("Sentiment:", prediction)
    else:
        st.write("Please enter a review.")


# In[ ]:




