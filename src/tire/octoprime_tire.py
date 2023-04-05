from src.tire.tire_interface import Tire

class OctoprimeTire(Tire):

    def __init__(self, tire_readings):
        super().__init__()
        self.tire_readings = tire_readings

    # override
    def needs_service(self) -> bool:
        """
        Octoprime tire needs to be replaced sum of the reading is larger 
        or equal to 3
        """
        return sum(self.tire_readings) >= 3.0