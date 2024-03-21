import paho.mqtt.client as mqtt
import pyodbc
import time
import random
from datetime import datetime

MQTT_SERVER = "mqtt.ohstem.vn"
MQTT_PORT = 1883
MQTT_USERNAME = "yolo"
MQTT_PASSWORD = ""
MQTT_TOPIC_SUB_V3 = MQTT_USERNAME + "/feeds/V3"
MQTT_TOPIC_SUB_V4 = MQTT_USERNAME + "/feeds/V4"


driver_name = "{ODBC Driver 17 for SQL Server}"
server_name = "DESKTOP-7CB1RAA"
database_name = "yolofarm"
conn_str = (
            f"DRIVER={driver_name};"
            f"SERVER={server_name};"
            f"DATABASE={database_name};"
            f"Trusted_Connection=yes;"
        )
# Create the connection to database
conn = pyodbc.connect(conn_str)

###########
temp = []
light = []
###########

def mqtt_connected(client, userdata, flags, rc):
    print("Connected succesfully to Ohstem server!!")
    client.subscribe(MQTT_TOPIC_SUB_V3)
    client.subscribe(MQTT_TOPIC_SUB_V4)

def mqtt_subscribed(client, userdata, mid, granted_qos):
    print("Subscribed to Topic!!!")

def mqtt_recv_message(client, userdata, message):
    if (message.topic == "yolo/feeds/V3"):
        temp.append(float(message.payload.decode("utf-8")))
    elif (message.topic == "yolo/feeds/V4"):
        light.append(float(message.payload.decode("utf-8")))

mqttClient = mqtt.Client()
mqttClient.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
mqttClient.connect(MQTT_SERVER, int(MQTT_PORT), 60)

#Register mqtt events
mqttClient.on_connect = mqtt_connected
mqttClient.on_subscribe = mqtt_subscribed
mqttClient.on_message = mqtt_recv_message

mqttClient.loop_start()


try:
    conn = pyodbc.connect(
    '''
    DRIVER={ODBC Driver 17 for SQL Server};
    SERVER=DESKTOP-7CB1RAA;
    DATABASE=yolofarm;
    Trusted_Connection=yes;
    '''
    )

    cursor = conn.cursor()

    cursor.execute("SELECT 1 AS test_value")
    result = cursor.fetchone()

    if result[0] == 1:
        print("Connection successful to SQL Server!")
    else:
        print("Unexpected query result.")

except pyodbc.Error as ex:
    print("Error connecting to database:", ex)


for i in range (0,5):
    time.sleep(3)
    # print("hello")
    now = datetime.now()
    temp = round(random.uniform(10, 40), 2)
    print("now =", now)
    print("temp =", temp)

    query = "INSERT INTO Temperature (Date_, Temp) VALUES (?, ?)"
    cursor.execute(query, now, temp)
    conn.commit()
    # print(temp)
    # print(light)
conn.close()



