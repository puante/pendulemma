import json

class DataLoad:
    def __init__(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def get_data(self):
        return self.data