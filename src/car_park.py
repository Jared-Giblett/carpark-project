from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime
import json

class CarPark:
    """
    A class to represent a car park
    ...
    Attributes
    ----------
    location : str
        location of the car park
    capacity : int
        how many bays are in the car park
    plates : list
        list of car plates
    sensors : list
        list of sensor objects
    displays : list
        list of display objects
    log_file : str
        name of the log_file
    config_file : str
        name of the config file

    Methods
    -------
    register(component)
        adds the component to the correct list (display or sensor)
    add_car(plate)
        adds the plate to the list
        updates the display
        log car activity
    remove_car(plate)
        removes the plate from the list
        updates the display
        log the car activity
    update_display()
        sends the data to the displays linked to the car park
    _log_car_activity(plate, action)
        write the car activity to the log file
    write_config()
        writes config to the config file json
    read_config()
        reads the json file to class
    """
    def __init__(self, location="Unknown",
                 capacity=100,
                 log_file=Path("log.txt"),
                 config_file=Path("config.json"),
                 plates=None,
                 sensors=None,
                 displays=None):
        # Initialize the car park
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)
        self.config_file = config_file

    def __str__(self):
        # returns a string with location and capacity
        return f"Car park at {self.location}, with {self.capacity} bays."


    def register(self, component):
        # Checks to see if the component is a sensor or display
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        # If component is sensor add to the sensor list
        if isinstance(component, Sensor):
            self.sensors.append(component)
        # If component is display add to the display list
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        # Adds car plate to the plate list
        self.plates.append(plate)
        # Update displays
        self.update_displays()
        # Log car to activity log
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        # Removes the plate form the list
        self.plates.remove(plate)
        # Updates the displays
        self.update_displays()
        # Logs car activity to log
        self._log_car_activity(plate, "exited")

    def update_displays(self):
        # Send the display data the displays
        data = {"Location": self.location, "available bays": self.available_bays, "temperature": 25}
        for display in self.displays:
            display.update(data)

    @property
    def available_bays(self):
        # Returns the number of bays available
        bays = self.capacity - len(self.plates)
        # If there is more cars in there than bays return 0
        if bays >= 0:
            return bays
        else:
            return 0

    def _log_car_activity(self, plate, action):
        # Write the plate and action (entered/exited) to file
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    def write_config(self):
        # Write the class to json
        with open(self.config_file, "w") as f:
            json.dump({"location": self.location,
                       "capacity": self.capacity,
                       "log_file": str(self.log_file)}, f)

    @classmethod
    def from_config(cls, config_file=Path("config.json")):
        # Read json file to class
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return cls(config["location"], config["capacity"], log_file=config["log_file"])
