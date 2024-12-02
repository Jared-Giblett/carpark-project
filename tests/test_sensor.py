import unittest
from sensor import EntrySensor, ExitSensor
from car_park import CarPark

class TestSensor(unittest.TestCase):
    def setUp(self):
        # Setup default Car Park and sensors
        self.car_park = CarPark("123 Example Street", 100)
        self.entry_sensor = EntrySensor(12, self.car_park, True)
        self.exit_sensor = ExitSensor(21, self.car_park, True)

    def test_entry_senor(self):
        # Testing entry sensor
        self.assertIsInstance(self.entry_sensor, EntrySensor)
        self.assertEqual(self.entry_sensor.id, 12)
        self.assertEqual(self.entry_sensor.is_active, True)

    def test_exit_senor(self):
        # Testing exit sensor
        self.assertIsInstance(self.exit_sensor, EntrySensor)
        self.assertEqual(self.exit_sensor.id, 21)
        self.assertEqual(self.exit_sensor.is_active, True)

    def test_detect_vehicle_entry(self):
        # Testing the entry numberplate
        self.entry_sensor.detect_vehicle("Test-01")
        self.assertEqual(self.car_park.plates[0], "Test-01")


if __name__ == "__main__":
   unittest.main()