class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculateArea(self):
        print("Area of rectangle: ", self.length * self.width)

rect = Rectangle(30, 25)
rect.calculateArea()