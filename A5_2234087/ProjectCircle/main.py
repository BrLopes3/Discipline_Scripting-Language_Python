"""
Assignment 5
Student: Bruno Lopes
Date: 2023-11-11

"""

from basisclasses.circle import Circle

if __name__ == "__main__":
    
    circle1 = Circle(2, 'blue')
    print(circle1.__str__())

    circle2 = Circle(3, 'green')
    print(circle2.__str__())

    circle3 = Circle(4) ## will be red by default
    print(circle3.__str__())

    circle4 = Circle(5, 'yellow')
    del circle4


