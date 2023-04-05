import unittest
from datetime import datetime

from src.car_factory import CarFactory


class TestCarFactory(unittest.TestCase):
    def test_calliope_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, [1.0, 0.3, 0.2, 0.9])
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = CarFactory.create_calliope(today, last_service_date, current_mileage, last_service_mileage, [0.8, 0.2, 0.8, 0.8])
        self.assertFalse(car.needs_service())

if __name__ == '__main__':
    unittest.main()
