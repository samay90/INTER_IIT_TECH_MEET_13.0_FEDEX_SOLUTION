import json

class ULD(object):

    def __init__(self, name, length, width, height, max_weight):
        self.name = name
        self.length = length
        self.width = width
        self.height = height
        self.max_weight = max_weight
        self.available_volume = length * width * height
        self.available_weight = max_weight
        self.packages = []
        self.ideal_density = max_weight / (length * width * height)

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
