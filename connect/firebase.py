import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

home_dir = os.getcwd()
relative_path = os.path.join(home_dir, "connect\yolofarm-92ca9-firebase-adminsdk-uwty3-af106b6fcd.json")
# Initialize Firebase Admin SDK
cred = credentials.Certificate(relative_path)
firebase_admin.initialize_app(cred)



class Temparature:
    def __init__(self, value, time):
        self.value = value
        self.time = time

    @staticmethod
    def from_dict(source):
        """Creates a Temperature object from a dictionary.
        KeyError: If the required keys ("value" or "time") are missing from the dictionary.
        TypeError: If the values for "value" or "time" are not of the expected types (float for value, string for time).
        """

        # Check for missing keys
        if "value" not in source or "time" not in source:
            raise KeyError("Missing required keys in dictionary: 'value' and 'time' are required.")

        # Check for value type
        if not isinstance(source["value"], float):
            raise TypeError("Value in dictionary must be a float.")

        # Check for time type
        if not isinstance(source["time"], str):
            raise TypeError("Time in dictionary must be a string.")

        # Extract and validate values
        value = source["value"]
        time = source["time"]

        # Create the Temperature object
        return Temparature(value, time)

    def to_dict(self):
        """Returns a dictionary representation of the Temperature object."""
        return {
            "value": self.value,
            "time": self.time
        }

    def __repr__(self):
        return f"Temperature(value={self.value}, time={self.time})"



db = firestore.client()
temp_ref = db.collection("temp") 
temp_ref.document("2").set(
    Temparature(27.5, "23-04-2024").to_dict()
)

# doc_snapshot = temp_ref.document("2").get()
# if doc_snapshot.exists:
#     data = doc_snapshot.to_dict()  # Use to_dict() for newer versions
#     temp_obj = Temparature.from_dict(data)
#     print(temp_obj)
# else:
#     print("Document does not exist!")

hehe = temp_ref.document("2").get().to_dict()
print(hehe)


