class Display:
    def __init__(self, id, car_park, data=None, is_on=False):
        self.id = id
        self.data = data or {}
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        return f"Display {self.id}: {self.data}"

    def update(self, data):
        self.data = data
        print("*"*80)
        print(f"Id: {self.id}")
        for key, value in self.data.items():
            print(f"{key}: {value}")
        print("*"*80)