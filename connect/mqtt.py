#pip install paho-mqtt==1.6.1
import paho.mqtt.client as mqtt
import time

MQTT_SERVER = "mqtt.ohstem.vn"
MQTT_PORT = 1883
MQTT_USERNAME = "yolo"
MQTT_PASSWORD = ""
# MQTT_TOPIC_PUB = MQTT_USERNAME + "/feeds/V3" # use for publish the data back to the feed
MQTT_TOPIC_SUB_V3 = MQTT_USERNAME + "/feeds/V3"
MQTT_TOPIC_SUB_V4 = MQTT_USERNAME + "/feeds/V4"
MQTT_TOPIC_SUB_V6 = MQTT_USERNAME + "/feeds/V3"
MQTT_TOPIC_SUB_V5 = MQTT_USERNAME + "/feeds/V4"

###########
temp = []
light = []
###########

def mqtt_connected(client, userdata, flags, rc):
    print("Connected succesfully!!")
    client.subscribe(MQTT_TOPIC_SUB_V3)
    client.subscribe(MQTT_TOPIC_SUB_V4)

def mqtt_subscribed(client, userdata, mid, granted_qos):
    print("Subscribed to Topic!!!")

def mqtt_recv_message(client, userdata, message):
    # print("Received: ", message.payload.decode("utf-8"))
    # print(" Received message " + message.payload.decode("utf-8")
    #       + " on topic '" + message.topic
    #       + "' with QoS " + str(message.qos))
    # global temp 
    # temp = message.payload.decode("utf-8")
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

while True:
    time.sleep(3)
    print(temp)
    print(light)
    # mqttClient.publish(MQTT_TOPIC_PUB, 1)