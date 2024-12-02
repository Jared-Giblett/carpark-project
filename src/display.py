class Display:
    """
    A class to display the car park data
    ...
    Attributes
    ----------
    id : int
        Hold the id of the display
    car_park : CarPark
        Holds the car park
    data : {}
        Holds the data to be displayed on the display
    is_on : bool
        Sets the display on and off
    """
    def __init__(self, id, car_park, data=None, is_on=False):
        self.id = id
        self.data = data or {}
        self.is_on = is_on
        self.car_park = car_park
        print(self.id)

    def __str__(self):
        return f"Display {self.id}: {self.data}"

    def update(self, data):
        # Updates the display with the latest data
        self.data = data
        print("*"*80)
        print(f"Id: {self.id}")
        for key, value in self.data.items():
            print(f"{key}: {value}")
        print("*"*80)