import json


class ConfigReader:
    _instance = None

    def __init__(self):
        with open("config.json") as file:
            self.config = json.load(file)

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = ConfigReader()

        return cls._instance

    def get(self, key):
        return self.config[key]