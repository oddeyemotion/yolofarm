import queue

MQTT_SERVER = "mqtt.ohstem.vn"
MQTT_PORT = 1883
MQTT_USERNAME = "yolo"
MQTT_PASSWORD = ""
# TODO: chọn kênh cho Yolo
MQTT_TOPIC_SUB_V1 = MQTT_USERNAME + "/feeds/V1"
MQTT_TOPIC_SUB_V2 = MQTT_USERNAME + "/feeds/V2"
MQTT_TOPIC_SUB_V3 = MQTT_USERNAME + "/feeds/V3"
MQTT_TOPIC_SUB_V4 = MQTT_USERNAME + "/feeds/V4"
MQTT_TOPIC_SUB_V5 = MQTT_USERNAME + "/feeds/V5"
MQTT_TOPIC_SUB_V6 = MQTT_USERNAME + "/feeds/V6"
###########
temp_queue = queue.Queue()
light_queue = queue.Queue()
humidAtm_queue = queue.Queue()
humidEarth_queue = queue.Queue()
###########


def mqtt_connected(client, userdata, flags, rc):
    print("Connected succesfully to Ohstem server!!")
    client.subscribe(MQTT_TOPIC_SUB_V5)
    client.subscribe(MQTT_TOPIC_SUB_V6)
    client.subscribe(MQTT_TOPIC_SUB_V3)
    client.subscribe(MQTT_TOPIC_SUB_V4)

def mqtt_subscribed(client, userdata, mid, granted_qos):
    print("Subscribed to Topic!!!")

# chỉnh lại cho phù hợp
def mqtt_recv_message(client, userdata, message):
    if (message.topic == "yolo/feeds/V3"):
        temp_queue.put(float(message.payload.decode("utf-8")))
    elif (message.topic == "yolo/feeds/V6"):
        light_queue.put(float(message.payload.decode("utf-8")))
    elif (message.topic == "yolo/feeds/V4"):
        humidAtm_queue.put(float(message.payload.decode("utf-8")))
    elif (message.topic == "yolo/feeds/V5"):
        humidEarth_queue.put(float(message.payload.decode("utf-8")))


class Record:
    def __init__(self, temp, flux, humidAtm, humidEarth, time):
        self.temp = temp
        self.flux = flux
        self.humidAtm = humidAtm
        self.humidEarth = humidEarth
        self.time = time

    @staticmethod
    def from_dict(source):

        # # Check for missing keys
        # if "temp" not in source or "flux" not in source or "humid" not in source or "time" not in source:
        #     raise KeyError("Missing required keys in dictionary")

        # # Check for temp type
        # if not isinstance(source["temp"], float):
        #     raise TypeError("Value in dictionary must be a float.")

        # # Check for flux type
        # if not isinstance(source["flux"], float):
        #     raise TypeError("Value in dictionary must be a float.")
        
        # # Check for humid type
        # if not isinstance(source["humid"], float):
        #     raise TypeError("Value in dictionary must be a float.")

        # # Check for time type
        # if not isinstance(source["time"], str):
        #     raise TypeError("Time in dictionary must be a string.")

        # Extract and validate values
        temp = source["temp"]
        flux = source["flux"]
        humidAtm = source["humidAtm"]
        humidEarth = source["humidEarth"]
        time = source["time"]

        # Create the Temperature object
        return Record(temp, flux, humidAtm, humidEarth, time)

    def to_dict(self):
        """Returns a dictionary representation of the Temperature object."""
        return {
            "temp": self.temp,
            "flux": self.flux,
            "humidAtm": self.humidAtm,
            "humidEarth": self.humidEarth,
            "time": self.time
        }

    def __repr__(self):
        return f"Record(temp={self.temp}, flux={self.flux}, humidAtm={self.humidAtm}, humidEarth={self.humidEarth}, time={self.time})"
    

