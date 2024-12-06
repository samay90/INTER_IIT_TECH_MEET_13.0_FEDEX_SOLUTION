import json

class Package(object):

    def __init__(self, name, length, width, height, weight, is_priority, delay_cost):


        self.name = name
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight
        self.density = weight / (length * width * height)
        self.volume = length * width * height
        self.is_priority = is_priority
        self.delay_cost = delay_cost
        self.x_dim = None
        self.y_dim = None
        self.z_dim = None
        self.COM = None
        self.uld_name = None
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
    def __str__(self):
        return f"Name: {self.name} - COM: {self.COM}"
