from flask import Flask, render_template, request, redirect, url_for, jsonify
import random
import queue
from utils import *
from main import *
from firebase_admin import firestore


db = firestore.client()
ref = db.collection("yolo") 

# from main import temp

# Create the Flask app
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

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5500)