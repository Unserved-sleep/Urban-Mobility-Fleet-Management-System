class Vehicle:
    def __init__(self, battery_percentage, maintenance_status, rental_price):
        self.__battery_percentage = 0
        self.__maintenance_status = maintenance_status
        self.__rental_price = rental_price

        self.set_battery_percentage(battery_percentage)

    def get_battery_percentage(self):
        return self.__battery_percentage

    def set_battery_percentage(self, value):
        if 0 <= value <= 100:
            self.__battery_percentage = value
        else:
            self.__battery_percentage = 0

    def get_maintenance_status(self):
        return self.__maintenance_status

    def set_maintenance_status(self, status):
        self.__maintenance_status = status

    def get_rental_price(self):
        return self.__rental_price

    def set_rental_price(self, value):
        self.__rental_price = value
