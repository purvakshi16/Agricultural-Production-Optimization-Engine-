from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import sklearn 
import pickle

#importing model

# with open('crop_recommendation.pkl','rb') as file:
# model = pickle.load(file)

model = pickle.load(open('crop_recommendation.pkl','rb'))
sc = pickle.load(open('standscaler.pkl','rb'))
ms = pickle.load(open('minmaxscaler.pkl','rb'))

#creating flask app
app = Flask(__name__)

@app.route('/')

def index():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])

def predict():
    #print(request.method)

    N = request.form['Nitrogen']
    P = request.form['Phosporus']
    K = request.form['Potassium']
    temp = request.form['Temperature']
    humidity = request.form['Humidity']
    ph = request.form['Ph']
    rainfall = request.form['Rainfall']

    feature_list = [N, P, K, temp, humidity, ph, rainfall]
    single_pred = np.array(feature_list).reshape(1, -1)

    scaled_features = ms.transform(single_pred)
    final_features = sc.transform(scaled_features)
    prediction = model.predict(final_features)

    crop_dict = {'rice': 1,'maize': 2,'chickpea': 3,'kidneybeans': 4,'pigeonpeas': 5,'mothbeans': 6,'mungbean': 7,'blackgram': 8,'lentil': 9,'pomegranate': 10,'banana': 11,'mango': 12,'grapes': 13,'watermelon': 14,'muskmelon': 15,'apple': 16,'orange':17,'papaya':18,'coconut':19,'cotton':20,'jute':21,'coffee' : 22 }

    if prediction[0] in crop_dict:
        crop = crop_dict[prediction[0]]
        result = "{} is the best crop to be cultivated right there".format(crop)
    else:
        result = "Sorry, we could not determine the best crop to be cultivated with the provided data."
        
    return render_template('index.html',result = result)

# python main

if __name__ == "__main__":
    app.run(debug=True)