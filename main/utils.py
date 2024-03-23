import queue

MQTT_SERVER = "mqtt.ohstem.vn"
MQTT_PORT = 1883
MQTT_USERNAME = "yolo"
MQTT_PASSWORD = ""
MQTT_TOPIC_SUB_V3 = MQTT_USERNAME + "/feeds/V3"
MQTT_TOPIC_SUB_V4 = MQTT_USERNAME + "/feeds/V4"


###########
temp_queue = queue.Queue()
light_queue = queue.Queue()
###########


def mqtt_connected(client, userdata, flags, rc):
    print("Connected succesfully to Ohstem server!!")
    client.subscribe(MQTT_TOPIC_SUB_V3)
    client.subscribe(MQTT_TOPIC_SUB_V4)

def mqtt_subscribed(client, userdata, mid, granted_qos):
    print("Subscribed to Topic!!!")

def mqtt_recv_message(client, userdata, message):
    if (message.topic == "yolo/feeds/V3"):
        # temp.append(float(message.payload.decode("utf-8")))
        temp_queue.put(float(message.payload.decode("utf-8")))
    elif (message.topic == "yolo/feeds/V4"):
        # light.append(float(message.payload.decode("utf-8")))
        light_queue.put(float(message.payload.decode("utf-8")))


class Record:
    def __init__(self, temp, flux, time):
        self.temp = temp
        self.flux = flux
        self.time = time

    @staticmethod
    def from_dict(source):
        """Creates a Temperature object from a dictionary.
        KeyError: If the required keys ("value" or "time") are missing from the dictionary.
        TypeError: If the values for "value" or "time" are not of the expected types (float for value, string for time).
        """

        # Check for missing keys
        if "temp" not in source or "flux" not in source or "time" not in source:
            raise KeyError("Missing required keys in dictionary: 'value' and 'time' are required.")

        # Check for temp type
        if not isinstance(source["temp"], float):
            raise TypeError("Value in dictionary must be a float.")

        # Check for temp type
        if not isinstance(source["flux"], float):
            raise TypeError("Value in dictionary must be a float.")

        # Check for time type
        if not isinstance(source["time"], str):
            raise TypeError("Time in dictionary must be a string.")

        # Extract and validate values
        temp = source["temp"]
        flux = source["flux"]
        time = source["time"]

        # Create the Temperature object
        return Record(temp, flux, time)

    def to_dict(self):
        """Returns a dictionary representation of the Temperature object."""
        return {
            "temp": self.temp,
            "flux": self.flux,
            "time": self.time
        }

    def __repr__(self):
        return f"Record(temp={self.temp}, flux={self.flux}, time={self.time})"
    

