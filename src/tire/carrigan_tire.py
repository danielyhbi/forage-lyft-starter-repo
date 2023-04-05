from src.tire.tire_interface import Tire

class CarriganTire(Tire):

    def __init__(self, tire_readings):
        super().__init__()
        self.tire_readings = tire_readings

    # override
    def needs_service(self) -> bool:
        """
        Carrigan tire needs to be replaced when any of the reading is
        larger or equal to 0.9
        """
        for number in self.tire_readings:
            if number >= 0.9:
                return True

        return False