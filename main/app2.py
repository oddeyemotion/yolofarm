from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS
# import random
# import queue
# from utils import *
# from main import *
from firebase_admin import firestore
import random
import numpy as np
import os
from pathlib import Path
import firebase_admin
from firebase_admin import credentials
from tensorflow.keras.models import load_model # type: ignore

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM

home_dir = os.getcwd()
path = Path(home_dir)
# print(path.parent.absolute())

# provide that you are staying at yolofarm/main folder
relative_path = os.path.join(path.parent, "connect\yolofarm-92ca9-firebase-adminsdk-uwty3-af106b6fcd.json")
# Initialize Firebase Admin SDK
cred = credentials.Certificate(relative_path)
firebase_admin.initialize_app(cred)

db = firestore.client()
ref = db.collection("yolo") 

# Create the Flask app
app = Flask(__name__)
# CORS(app)

# Define a route
@app.route('/')
def hello_world():
    return render_template("index.html")

data_storage = []
@app.route('/record_data')
def record_data():
    # get the latest record
    # docs = ref.order_by('time', direction=firestore.Query.DESCENDING).limit(1).get()
    # doc = docs[0]
    # temp_data = doc.to_dict()

    data = {
        'temp': random.uniform(10, 40),
        'flux': random.uniform(10, 40),
        'humidAtm': random.uniform(10, 40),
        'humidEarth': random.uniform(10, 40),
        'timestamp': ''
    }
    return jsonify({'message': 'Data recorded', 'data': data})

relative_path_2 = os.path.join(path.parent, "model\model.h5")
model = load_model(relative_path_2)
@app.route('/predict_temperature', methods=['POST'])
def predict_temperature():
    data = request.get_json()
    # Assume the input data is in the correct shape for your model
    # input_data = np.array(data['input']).reshape(1, -1)
    input_data= np.array(data['input'])
    print(input_data)
    prediction = model.predict(input_data)
    temp = prediction[0][0]
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return jsonify({'temperature': float(temp), 'timestamp': ''})


# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5500)