class CarPark:
    def __init__(self, location="Unknown", capacity=100, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates
        self.sensors = sensors
        self.displays = displays

    def __str___(self):
        return f"Car park at {self.location}, with {self.capacity} bays."
