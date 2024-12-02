import unittest
from display import Display
from car_park import CarPark

class TestDisplay(unittest.TestCase):
    def setUp(self):
        # Setup the default Car Park and Display
        self.car_park = CarPark("123 Example Street", 100)
        self.display = Display(1, self.car_park,"Welcome to the car park", True)

    def test_display_initialized_with_all_attributes(self):
        # Test initialization of the display
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.id, 1)
        self.assertEqual(self.display.data, "Welcome to the car park")
        self.assertEqual(self.display.is_on, True)
        self.assertIsInstance(self.display.car_park, CarPark)

    def test_update(self):
        # Test updating message on display
        self.display.update({"message": "Goodbye"})
        self.assertEqual(self.display.data, {"message": "Goodbye"})


if __name__ == "__main__":
   unittest.main()