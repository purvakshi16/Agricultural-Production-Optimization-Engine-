Crop Recommendation System 🌾
Overview
The Crop Recommendation System is a machine learning-based project that predicts the most suitable crop to grow based on climatic and soil conditions. By leveraging data science techniques, this system aims to support farmers and agricultural stakeholders in making informed decisions to enhance productivity and sustainability.

Features
Predicts suitable crops based on inputs like Nitrogen, Phosphorus, Potassium, temperature, humidity, pH, and rainfall.
Implements MinMaxScaler for data preprocessing to ensure scaled and consistent inputs.
Trains and evaluates multiple machine learning models, including Random Forest and Logistic Regression.
Achieves a high prediction accuracy of 95% using the optimized Random Forest model.
Saves the trained model and scaler using pickle for deployment and real-time predictions.

Technologies Used
Programming Language: Python
Libraries: Pandas, NumPy, Scikit-learn
Tools: MinMaxScaler, Random Forest Classifier, pickle

Dataset
The dataset includes climatic and soil condition features:

Features: Nitrogen (N), Phosphorus (P), Potassium (K), Temperature, Humidity, pH, Rainfall
Target: Crop category (22 unique crops)

How to Use
Prerequisites
Python 3.7 or later
Required libraries: pandas, numpy, scikit-learn, flask
Installation
Clone the repository:
