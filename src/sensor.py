from abc import ABC, abstractmethod
import random

# Abstract class for sensors
class Sensor(ABC):
    """
    An abstract class for sensors
    ...
    Attributes
    ----------
    id : int
        The id of the sensor
    is_active : bool
        Switch to set the sensor active/inactive
    car_park : CarPark
        The car park object
    """
    def __init__(self, id, car_park, is_active=False):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        return f"Sensor {self.id} is {self.is_active}"

    @abstractmethod
    def update_car_park(self, plate):
        pass

    def _scan_plate(self):
        # Creates a fake plate
        return 'FAKE-' + format(random.randint(0, 999), "03d")

    def detect_vehicle(self):
        # Detects the vehicle
        plate = self._scan_plate()
        self.update_car_park(plate)

class EntrySensor(Sensor):
    # The entry sensor
    def detect_vehicle(self):
        # Detects the plate of the incoming car
        plate = self._scan_plate()
        self.car_park.add_car(plate)
        print(f"Incoming vehicle detected: Plate :{plate}")

    def update_car_park(self, plate):
        ...

class ExitSensor(Sensor):
    # The exit sensor
    def detect_vehicle(self):
        # Detects the plate of the outgoing car
        plate = self._scan_plate()
        self.car_park.remove_car(plate)
        print(f"Outgoing vehicle detected: Plate :{plate}")


    def update_car_park(self, plate):
        ...

    def _scan_plate(self):
        # Returns a plate from the list of plates
        return random.choice(self.car_park.plates)