# Crop Recommendation System 🌾
## Overview
The Crop Recommendation System is a machine learning-based project that predicts the most suitable crop to grow based on climatic and soil conditions. By leveraging data science techniques, this system aims to support farmers and agricultural stakeholders in making informed decisions to enhance productivity and sustainability.

## Features
  * Predicts suitable crops based on inputs like Nitrogen, Phosphorus, Potassium, temperature, humidity, pH, and rainfall.
  *Implements MinMaxScaler for data preprocessing to ensure scaled and consistent inputs.
  *Trains and evaluates multiple machine learning models, including Random Forest and Logistic Regression.
  *Achieves a high prediction accuracy of 95% using the optimized Random Forest model.
  *Saves the trained model and scaler using pickle for deployment and real-time predictions.

## Technologies Used
### Programming Language: Python
### Libraries: Pandas, NumPy, Scikit-learn
### Tools: MinMaxScaler, Random Forest Classifier, pickle

## Dataset
The dataset includes climatic and soil condition features:

Features: Nitrogen (N), Phosphorus (P), Potassium (K), Temperature, Humidity, pH, Rainfall
Target: Crop category (22 unique crops)

## Model Training
 * Split the dataset into training (80%) and testing (20%) subsets.
 *Applied MinMaxScaler to preprocess data and scale features.
 *Trained and compared 10+ machine learning models, selecting Random Forest for deployment due to its high accuracy.

## Installation
To set up the project locally, follow these steps:

### 1. Clone the Repository:
```
git clone https://github.com/purvakshi16/crop-recommendation-system.git
cd crop-recommendation-system

```
### 2. Install the Required Packages:
```
pip install -r requirements.txt

```
### 3. Run the flask application:
```
python app.py

```
### 4. Access the Web Application:
http://127.0.0.1:5000/

## Prediction
Enter inputs like Nitrogen, Phosphorus, and other parameters.
The model predicts the most suitable crop based on the given inputs.

# Results
Prediction Accuracy: 95%
Top Features: Nitrogen, Phosphorus, Potassium, Rainfall
Models Evaluated: Random Forest, Logistic Regression, SVM, Naive Bayes, etc.

# Future Scope
Extend the model to include real-time data inputs from IoT devices.
Integrate market price predictions for better decision-making.
Deploy the application as a mobile app for accessibility.


