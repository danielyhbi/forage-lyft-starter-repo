import unittest

from src.tire.carrigan_tire import CarriganTire
from src.tire.octoprime_tire import OctoprimeTire

class TestTires(unittest.TestCase):
    def test_carrigan_needs_service_true(self):
        tire_wear = [1.0, 0.3, 0.2, 0.9]
        tires = CarriganTire(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_carrigan_needs_service_false(self):
        tire_wear = [0.8, 0.2, 0.8, 0.8]
        tires = CarriganTire(tire_wear)
        self.assertFalse(tires.needs_service())

    def test_octoprime_needs_service_true(self):
        tire_wear = [1.0, 1.0, 0.2, 0.9]
        tires = OctoprimeTire(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_octoprime_needs_service_false(self):
        tire_wear = [0.8, 0.2, 0.8, 0.8]
        tires = OctoprimeTire(tire_wear)
        self.assertFalse(tires.needs_service())
