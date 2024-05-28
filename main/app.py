from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, jsonify
import random
import queue
from utils import *
from main import *
from firebase_admin import firestore


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
    temp = random.randint(20, 35)
    flux = random.randint(100, 1000)
    humid = random.randint(20, 80)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data_storage.append({'temp': temp, 'flux': flux, 'timestamp': timestamp})
    return jsonify({'message': 'Data recorded', 'data': {'temp': temp, 'flux': flux, 'timestamp': timestamp}})


# @app.route('/get_number')
# def get_number():
#     # temp = round(random.uniform(10, 40), 2)
#     # flux = round(random.uniform(0, 100), 2)
#     res = ref.document("1").get().to_dict()
#     # last_doc = ref.order_by("id", direction=firestore.Query.DESCENDING).limit(1).get().to_dict()
#     # return jsonify({'temp': temp, 'flux':flux})
#     return res

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5500)