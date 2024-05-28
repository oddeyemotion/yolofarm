from flask import Flask, render_template, request, redirect, url_for, jsonify
import random
import queue
import os
from utils import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from pathlib import Path


home_dir = os.getcwd()
path = Path(home_dir)
print(path.parent.absolute())

# provide that you are staying at yolofarm/main folder
relative_path = os.path.join(path.parent, "connect\yolofarm-92ca9-firebase-adminsdk-uwty3-21e21c3d97.json")
# Initialize Firebase Admin SDK
cred = credentials.Certificate(relative_path)
firebase_admin.initialize_app(cred)

db = firestore.client()
ref = db.collection("yolo") 

# Create the Flask apps
app = Flask(__name__)

# Define a route
@app.route('/')
def hello_world():
    # number = generate_number()
    # return render_template("index.html", number = number)
    return render_template("index.html")

@app.route('/get_number')
def get_number():
    # temp = round(random.uniform(10, 40), 2)
    # flux = round(random.uniform(0, 100), 2)
    res = ref.document("1").get().to_dict()
    # last_doc = ref.order_by("id", direction=firestore.Query.DESCENDING).limit(1).get().to_dict()
    # return jsonify({'temp': temp, 'flux':flux})
    return res

data_storage = []

@app.route('/record_data')
def record_data():
    # Ghi lại dữ liệu mỗi lần gọi API này
    temp = random.randint(20, 35)
    flux = random.randint(100, 1000)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data_storage.append({'temp': temp, 'flux': flux, 'timestamp': timestamp})
    return jsonify({'message': 'Data recorded', 'data': {'temp': temp, 'flux': flux, 'timestamp': timestamp}})

@app.route('/get_data')
def get_data():
    # Trả về dữ liệu đã ghi
    return jsonify(data_storage)

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5500)