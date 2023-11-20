"""
Create the class Person with the following characterises:
    Attributes:
▪ Last Name
▪ First Name
▪ Phone type

"""

class Person:

    ## parameterized constructor
    def __init__(self, last_name, first_name, phone_type):
        self._last_name = last_name
        self._first_name = first_name
        self._phone_type = phone_type

    ## getters
    def getLastName(self):
        return self._last_name
    
    def getFirstName(self):
        return self._first_name
    
    def getPhoneType(self):
        return self._phone_type
    
    ## setters

    def setLastName(self, lastName):
        self._last_name = lastName

    def setFirstName(self, firstName):
        self._first_name = firstName

    def setPhoneType(self, phoneType):
        self._phone_type = phoneType
    
    ## toString method
    def __str__(self):
        return f"First Name: {self._first_name}, Last Name: {self._last_name}, Phone: {self._phone_type}"