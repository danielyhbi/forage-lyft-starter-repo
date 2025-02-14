from abc import ABC
from datetime import date
from src.car import Car
from src.engine.capulet_engine import CapuletEngine
from src.engine.sternman_engine import SternmanEngine
from src.engine.willoughby_engine import WilloughbyEngine
from src.battery.spindler_battery import SpindlerBattery
from src.battery.nubbin_battery import NubbinBattery
from src.tire.octoprime_tire import OctoprimeTire
from src.tire.carrigan_tire import CarriganTire


class CarFactory:
    """
    Generate car objects using the factory design pattern
    """

    @staticmethod
    def create_calliope(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
        tire_reading
    ) -> Car:
        return Car(
            CapuletEngine(current_mileage, last_service_mileage),
            SpindlerBattery(current_date, last_service_date),
            CarriganTire(tire_reading),
        )

    @staticmethod
    def create_glissade(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
        tire_reading
    ) -> Car:
        return Car(
            WilloughbyEngine(current_mileage, last_service_mileage),
            SpindlerBattery(current_date, last_service_date),
            OctoprimeTire(tire_reading),
        )

    @staticmethod
    def create_palindrome(
        current_date: date, last_service_date: date, warning_light_on: bool, tire_reading
    ) -> Car:
        return Car(
            SternmanEngine(warning_light_on),
            SpindlerBattery(current_date, last_service_date),
            CarriganTire(tire_reading),
        )

    @staticmethod
    def create_rorschach(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
        tire_reading
    ) -> Car:
        return Car(
            WilloughbyEngine(current_mileage, last_service_mileage),
            NubbinBattery(current_date, last_service_date),
            OctoprimeTire(tire_reading),
        )

    @staticmethod
    def create_thovex(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
        tire_reading
    ) -> Car:
        return Car(
            CapuletEngine(current_mileage, last_service_mileage),
            NubbinBattery(current_date, last_service_date),
            CarriganTire(tire_reading),
        )
