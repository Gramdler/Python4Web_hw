import json, pickle
from abc import abstractmethod, ABC

class SerializationInterface(ABC):
    @abstractmethod
    def serialize(self, data):
        pass

    @abstractmethod
    def deserialize(self, file_name):
        pass

class Serialize_json(SerializationInterface):
    def serialize(self, data):
        with open("data.json", "w") as fh:
            json.dump(data, fh)

    def deserialize(self, file_name):
        with open(file_name, "r") as fh:
            result = json.load(fh)
            return print(result)

class Serialize_bin(SerializationInterface):
    def serialize(self, data):
        with open("data.bin", "wb") as fh:
            pickle.dump(data, fh)

    def deserialize(self, file_name):
        with open(file_name, "rb") as fh:
            result = pickle.load(fh)
            return print(result)

if __name__=="__main__":

    data = {'key': 'value', 2: [1, 2, 3], 'tuple': (5, 6), 'a': {'key': 'value'}}

    j = Serialize_json()

    j.serialize(data)
    j.deserialize("data.json")

    t = Serialize_bin()

    t.serialize(data)
    t.deserialize("data.bin")