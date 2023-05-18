# movie_review_analysis

The Movie Review Analysis App is a web application that uses Natural Language Processing (NLP) techniques to analyze the sentiment of movie reviews. It allows users to input their own text and get predictions on whether the sentiment of the text is positive or negative.

Data:-
The sentiment analysis model used in this app was trained on an IMDb movie review dataset. The dataset consists of movie reviews labeled as positive or negative sentiment. If you wish to use your own dataset, make sure it follows a similar format with labeled sentiment for training a new model.

Features:-
User-friendly interface: The web application provides an intuitive interface for users to enter their movie review text.
Sentiment analysis: The app utilizes a trained machine learning model to analyze the sentiment of the inputted movie review.
Easy deployment: The app is deployed using Streamlit, a Python library for building interactive web applications.

Here's the link of the app:
https://megharaj24-movie-review-analysis-app-qlpvhg.streamlit.app/
![interface](https://github.com/megharaj24/movie_review_analysis/assets/91184652/699f9ce9-1029-4251-8b07-82c706160afa)

Usage:-
Enter your movie review text in the provided input box.
Click the "Predict Sentiment" button to initiate the sentiment analysis.
The app will display the predicted sentiment (positive or negative).

Technologies Used:-
Python
Streamlit
scikit-learn
pandas
numpy

Installation and Setup:-
Step1- Clone the repository or download the source code.

Step2-Install the required dependencies by running the following command:
CODE-
pip install -r requirements.txt

Step3-Run the app using Streamlit:
CODE-
streamlit run app.py

Step4-Open a web browser and navigate to http://localhost:8501 to access the Movie Review Analysis App.

Acknowledgements:-
The development of this app was inspired by the need to analyze sentiments in movie reviews. It utilizes the power of NLP and machine learning techniques. Special thanks to the developers and contributors of the open-source libraries and frameworks used in this project.
