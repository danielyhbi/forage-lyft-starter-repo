from battery_interface import Battery
from utils.add_years_to_date import add_years_to_date

class SpindlerBattery(Battery):
    """
    Class for the Splinder battery (concrete)
    """

    def __init__(self, current_date: int, last_service_date: int) -> None:
        super().__init__()
        self.current_date = current_date
        self.last_service_date = last_service_date

    def get_current_date(self) -> int:
        return self.current_date
    
    def get_last_service_date(self) -> int:
        return self.last_service_date
    
    # override
    def needs_service(self) -> bool:
        """
        Battery needs to be replaced every 2 years
        """
        next_service_date = add_years_to_date(self.current_date, 2)
        return next_service_date < self.current_date
