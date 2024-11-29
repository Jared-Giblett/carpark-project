from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

def main():
    car_park1 = CarPark("Moondalup", 100, "log.txt")
    entry_sensor1 = EntrySensor(1, car_park1, True)
    exit_sensor1 = ExitSensor(2, car_park1, True)
    display = Display(1, car_park1, "Welcome to Moondalup", True)
    print(car_park1.__str__())
    car_park1.register(entry_sensor1)
    car_park1.register(exit_sensor1)
    car_park1.register(display)
    for number in range(10):
        car_park1.sensors[0].detect_vehicle()
    car_park1.sensors[1].detect_vehicle()
    car_park1.sensors[1].detect_vehicle()



if __name__ == '__main__':
    main()