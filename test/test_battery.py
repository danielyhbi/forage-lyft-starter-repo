import unittest
from datetime import date

from src.battery.spindler_battery import SpindlerBattery
from src.battery.nubbin_battery import NubbinBattery

class TestBattery(unittest.TestCase):
    def test_spindler_needs_service_true(self):
        current_date = date.fromisoformat("2023-04-04")
        last_service_date = date.fromisoformat("2020-04-03")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_spindler_needs_service_false(self):
        current_date = date.fromisoformat("2023-04-04")
        last_service_date = date.fromisoformat("2020-04-05")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

    def test_nubbin_needs_service_true(self):
        current_date = date.fromisoformat("2023-04-04")
        last_service_date = date.fromisoformat("2017-04-03")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_nubbin_needs_service_false(self):
        current_date = date.fromisoformat("2023-04-04")
        last_service_date = date.fromisoformat("2020-04-05")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())