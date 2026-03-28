class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def display_info(self):
        print("-------Car Info--------")
        print("brand:", self.brand)
        print("model:", self.model)
        print("year:", self.year)

car1 = Car("Honda", "Civic", 2026)
car1.display_info()

car2 = Car("Honda", "Accord", 2014)
car2.display_info()