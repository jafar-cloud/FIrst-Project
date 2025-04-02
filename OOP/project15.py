class Vehicle():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.rental_price_per_day = 0

    def calculate_rental_cost(self, days):
        return self.rental_price_per_day * days


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.rental_price_per_day = 100
    

class Bike(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.rental_price_per_day = 50


class Truck(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.rental_price_per_day = 200


class RentalService:
    def __init__(self, vehicle: Vehicle, days):
        self.vehicle = vehicle
        self.days = days

    def calculate_rental_cost(self):
        print(f"Total rental cost is {self.vehicle.calculate_rental_cost(self.days)}")
        return self.vehicle.calculate_rental_cost(self.days)
    

a = Car("Toyota", "Coroola")

rental_serv = RentalService(a, 3)

rental_serv.calculate_rental_cost()