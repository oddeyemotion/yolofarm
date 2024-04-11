import sys
import paho.mqtt.client as paho

def on_message(client, userdata, msg):
    print(msg.topic + ": " + msg.payload.decode())

client = paho.Client()
client.on_message = on_message

if client.connect("localhost", 1883, 60) != 0:
    print("Couldn't connect to MQTT broker!")
    sys.exit(-1)

client.subscribe("test/status")

try:
    print("Press CTRL+C to exit")
    client.loop_forever()
except:
    print("Exiting...")

client.disconnect()