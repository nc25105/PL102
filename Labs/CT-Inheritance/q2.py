class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model
    def display_car(self):
        print("Car brand: ", self.brand)
        print("Car year: ", self.year)
        print("Car model: ", self.model)

Car1 = Car("Toyota", 2012, "RAV4")
Car1.display_car()