class Vehicle:
    vehicle_type = "none"


class Car:
    price = 1000000

    def horse_powers(self):
        return

class Nissan(Car, Vehicle):
    price = 800000
    vehicle_type = True

    def __init__(self):
        self.hp = int

    def horse_powers(self):
        self.hp = 105


car1 = Nissan()
print(car1.vehicle_type)
print(car1.price)