"""
Assignmet 5
Student: Bruno Lopes
Date: 2023-11-11

3) Create the class Circle with the following characteristics:

"""

class Circle:

    # Class attribute
    __circleCount = 0

    # Constructor
    def __init__(self, radius, color = 'red'):
        Circle.__circleCount += 1
        self.__circleId = f"CIR_{Circle.__circleCount}"
        self.__radius = radius
        self.__color = color

    # Getters and Setters
    def getCircleId(self):
        return self.__circleId

    def getRadius(self):
        return self.__radius

    def getColor(self):
        return self.__color

    def setRadius(self, radius):
        self.__radius = radius

    def setColor(self, color):
        self.__color = color

    # Methods
    def calcArea(self):
        return 3.14 * self.__radius * self.__radius
    
    def calcPerimeter(self):
        return 2 * 3.14 * self.__radius


    def __str__(self):
        return f"Circle Id: {self.__circleId}, Radius: {self.__radius}, Color: {self.__color}, Perimeter: {self.calcPerimeter()}, Area: {self.calcArea()}"

    def __del__(self):
        print(f"Circle {self.__circleId} has been deleted.")
        Circle.__circleCount -= 1
    
