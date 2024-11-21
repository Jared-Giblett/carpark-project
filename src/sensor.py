class Sensor:
    def __init__(self, id=404, is_active=False, car_park=None):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        return f"Senser {self.id} is {self.is_active}"

class EntrySenser(Sensor):
    ...

class ExitSenser(Sensor):
    ...