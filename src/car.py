from src.engine.engine_interface import Engine
from src.battery.battery_interface import Battery
from src.tire.tire_interface import Tire
from src.utils.serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery, tire: Tire):
        super().__init__
        self.engine = engine
        self.battery = battery
        self.tire = tire

    # override
    def needs_service(self) -> bool:
        """
        Determines if a car needs service by checking both engine and battery
        """
        return self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service()
