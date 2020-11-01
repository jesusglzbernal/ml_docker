import numpy as np
import sys
from sklearn.ensemble import RandomForestClassifier
from flask import Flask, request
from pickle import load

# Load the model
with open('../model/rf_model.pkl', 'rb') as model_file:
    model = load(model_file)


# Create the API endpoint
def predict_wbc():
    # Reading the request values
    a1 = 1
    a2 = 1
    a3 = 1
    a4 = 1
    a5 = 1
    a6 = 1
    a7 = 1
    a8 = 1
    a9 = 1
    # Use the model to predict the new instance obtained through the API
    new_instance = np.array([[a1, a2, a3, a4, a5, a6, a7, a8, a9]])
    pred = model.predict(new_instance)

    # Return the prediction
    return 'Prediction for the new instance: ' + str(pred)

print(predict_wbc())
