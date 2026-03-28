class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculateArea(self):
        print("Area of rectangle: ", self.length * self.width)
    def calculatePerimeter(self):
        print("Perimeter of rectangle: ", 2*(self.length + self.width))

rect = Rectangle(10, 5)
rect.calculatePerimeter()