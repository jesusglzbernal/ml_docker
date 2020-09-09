import numpy as np
import pandas as pd
import sys
from sklearn.ensemble import RandomForestClassifier
from flask import Flask, request, jsonify, Response
from pickle import load


# Load the model stored in a pickle file
with open('src/rf_model.pkl', 'rb') as model_file:
    model = load(model_file)

predictors = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9']


# Initialize the Flask app
app = Flask(__name__)

# Create the API endpoint
@app.route('/predict', methods=['POST'])
def predict_wbc():
    my_file = request.files['file']
    data = pd.read_csv(my_file)
    
    # Use the model to predict the new instance obtained through the API
    pred = model.predict(data[predictors]) # The prediction of the new instance
    data['class'] = pred
    # Return the prediction
    return Response(data.to_json(orient="records"), mimetype='application/json') #'Prediction for the new instances: ' + str(pred) + '\n\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0') # Allow the container run in the local ip address
                            # by using the parameter host='0.0.0.0'
