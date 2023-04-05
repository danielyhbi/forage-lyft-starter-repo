from datetime import date
from src.battery.battery_interface import Battery
from src.utils.add_years_to_date import add_years_to_date

class NubbinBattery(Battery):
    """
    Class for the Nubbin battery (concrete)
    """

    def __init__(self, current_date: date, last_service_date: date) -> None:
        super().__init__()
        self.current_date = current_date
        self.last_service_date = last_service_date

    def get_current_date(self) -> date:
        return self.current_date
    
    def get_last_service_date(self) -> date:
        return self.last_service_date
    
    # override
    def needs_service(self) -> bool:
        """
        Nubbin Battery needs to be replaced every 4 years
        """
        next_service_date = add_years_to_date(self.last_service_date, 4)
        return next_service_date < self.current_date
