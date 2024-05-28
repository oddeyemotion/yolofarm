import paho.mqtt.client as mqtt
import time
import random
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
from pathlib import Path
from utils import *
# from utils import temp_queue, light_queue
import threading
import queue


home_dir = os.getcwd()
path = Path(home_dir)
# print(path.parent.absolute())

# provide that you are staying at yolofarm/main folder
relative_path = os.path.join(path.parent, "connect\yolofarm-92ca9-firebase-adminsdk-uwty3-af106b6fcd.json")
# Initialize Firebase Admin SDK
cred = credentials.Certificate(relative_path)
firebase_admin.initialize_app(cred)


##########
mqttClient = mqtt.Client()
mqttClient.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
mqttClient.connect(MQTT_SERVER, int(MQTT_PORT), 60)
# Register mqtt events
mqttClient.on_connect = mqtt_connected
mqttClient.on_subscribe = mqtt_subscribed
mqttClient.on_message = mqtt_recv_message
mqttClient.loop_start()

db = firestore.client()
ref = db.collection("yolo") 


# get 5 latest records
# docs = ref.order_by('time', direction=firestore.Query.DESCENDING).limit(5).get()
# for doc in docs:
#     print(f'{doc.id} => {doc.to_dict()}')

def mqtt_task():
    id = 0
    while True:
        # update to database
        time.sleep(1.5)
        now = datetime.now()
        # temp = round(random.uniform(10, 40), 2)
        # flux = round(random.uniform(10, 40), 2)
        # humidAtm = round(random.uniform(10, 40), 2)
        # humidEarth = round(random.uniform(10, 40), 2)

        temp = temp_queue.get()
        flux = light_queue.get()
        humidAtm = humidAtm_queue.get()
        humidEarth = humidEarth_queue.get()
        ref.document(str(id)).set(Record(temp, flux, humidAtm, humidEarth, now).to_dict())
        id += 1


mqtt_thread = threading.Thread(target=mqtt_task)
mqtt_thread.start()





