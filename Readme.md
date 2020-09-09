# ml_docker

In this repository you will find how to contenerize a machine learning model using docker.
This example uses the Wisconsin Breast Cancer dataset from the UCI Machine Learning Repository


The directory structure of this repo:

- ml_docker, the root directory
    - wbc_predict, the code to containerize our prediction app for the Wisconsin Breast Cancer dataset
        - src, directory for the source code of the app
            - main.py, the flask app that calls the predict function to provide the prediction for new samples
            - rf_model.pkl, the random forest model created for the Wisconsin Breast Cancer dataset
        - Dockerfile, the Dockerfile containing the specification of the image creation
        - requirements.txt, the required libraries to install in the container
    - wbc_predict_file

## Steps to build your image and run your container in your local machine
1. In order to build your image:
    - Clone this repo
    - $ cd wbc_predict/src
    - $ sudo docker image build -t "wbc_predict" .
2. To start your container:
    - $ sudo docker run -p 5000:5000 wbc_predict
3. To test your container for a single instance you need to call main_single.py in your Dockerfile
    - Call the API using the link: http://localhost:5000/predict?a1=1&a2=1&a3=1&a4=1&a5=1&a6=1&a7=1&a8=1&a9=1
    - a1 to a9 correspond to the attribute values of a sample to make a prediction
    - You can also use postman to test your API
4. To test your container with batch scoring you need to call main_batch.py in your Dockerfile
    - Call the API using curl:
    - $ curl -v -F 'file=@test.csv' http://localhost:5000/predict

