from sensor import Sensor
from display import Display

class CarPark:
    def __init__(self, location="Unknown", capacity=100, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates
        self.sensors = sensors
        self.displays = displays

    def __str___(self):
        return f"Car park at {self.location}, with {self.capacity} bays."


    def register(self, component):
        if not isinstance(component, (Sensor, Display))
            raise TypeError("Object must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)