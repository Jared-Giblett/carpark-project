from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

def main():
    # Create a car park object
    car_park1 = CarPark("Moondalup", 100, "log.txt")
    # Creates an entry sensor
    entry_sensor1 = EntrySensor(1, car_park1, True)
    # Creates an exit sensor
    exit_sensor1 = ExitSensor(2, car_park1, True)
    # Creates a display object
    display = Display(1, car_park1, "Welcome to Moondalup", True)
    print(car_park1.__str__())
    # Registers the entry sensor with the car park
    car_park1.register(entry_sensor1)
    # Registers the exit sensor with the car park
    car_park1.register(exit_sensor1)
    # Registers the display with the car park
    car_park1.register(display)
    # Add 10 cars to the car park
    for number in range(10):
        car_park1.sensors[0].detect_vehicle()
    # Remove 2 carw from the car park
    car_park1.sensors[1].detect_vehicle()
    car_park1.sensors[1].detect_vehicle()



if __name__ == '__main__':
    main()