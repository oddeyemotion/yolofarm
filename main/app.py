from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, jsonify
import random
import queue
from utils import *
from main import *
from firebase_admin import firestore

# import os
# from pathlib import Path
# import firebase_admin
# from firebase_admin import credentials

# home_dir = os.getcwd()
# path = Path(home_dir)
# # print(path.parent.absolute())

# # provide that you are staying at yolofarm/main folder
# relative_path = os.path.join(path.parent, "connect\yolofarm-92ca9-firebase-adminsdk-uwty3-af106b6fcd.json")
# # Initialize Firebase Admin SDK
# cred = credentials.Certificate(relative_path)
# firebase_admin.initialize_app(cred)

db = firestore.client()
ref = db.collection("yolo") 

# Create the Flask app
app = Flask(__name__)

# Define a route
@app.route('/')
def hello_world():
    number = round(random.uniform(10, 40), 2)
    # return render_template("index.html", number = number)
    return render_template("index.html", number = number)

data_storage = []
@app.route('/record_data')
def record_data():
    # get 5 latest records
    # docs = ref.order_by('time', direction=firestore.Query.DESCENDING).limit(5).get()
    # for doc in docs:
    #     print(f'{doc.id} => {doc.to_dict()}')
    # get the latest record
    docs = ref.order_by('time', direction=firestore.Query.DESCENDING).limit(1).get()
    doc = docs[0]
    temp_data = doc.to_dict()
    print(temp_data)
    timestamp = ''
    # data_storage.append({'temp': temp, 'flux': flux, 'timestamp': timestamp})
    data = {
        'temp': temp_data['temp'],
        'flux': temp_data['flux'],
        'humidAtm': temp_data['humidAtm'],
        'humidEarth': temp_data['humidEarth'],
        'timestamp': ''
    }
    return jsonify({'message': 'Data recorded', 'data': data})



# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5500)