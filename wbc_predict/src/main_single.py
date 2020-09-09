import numpy as np
import sys
from sklearn.ensemble import RandomForestClassifier
from flask import Flask, request
from pickle import load

# Load the model stored in a pickle file
with open('src/rf_model.pkl', 'rb') as model_file:
    model = load(model_file)

# Initialize the Flask app
app = Flask(__name__)

# Create the API endpoint
@app.route('/predict')
def predict_wbc():
    # Reading the request values, the feature values for the new sample
    a1 = request.args.get('a1')
    a2 = request.args.get('a2')
    a3 = request.args.get('a3')
    a4 = request.args.get('a4')
    a5 = request.args.get('a5')
    a6 = request.args.get('a6')
    a7 = request.args.get('a7')
    a8 = request.args.get('a8')
    a9 = request.args.get('a9')
    
    # Use the model to predict the new instance obtained through the API
    new_instance = np.array([data])
    pred = model.predict(new_instance) # The prediction of the new instance

    # Return the prediction
    return 'Prediction for the new instance: ' + str(pred)

if __name__ == '__main__':
    app.run(host='0.0.0.0') # Allow the container run in the local ip address
                            # by using the parameter host='0.0.0.0'
