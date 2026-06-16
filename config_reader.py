import json


class ConfigReader:
    _instances = {}

    def __init__(self, file_name):
        with open(file_name) as file:
            self.config = json.load(file)

    @classmethod
    def get_instance(cls, file_name="config.json"):
        if file_name not in cls._instances:
            cls._instances[file_name] = ConfigReader(file_name)

        return cls._instances[file_name]

    def get(self, key):
        return self.config[key]