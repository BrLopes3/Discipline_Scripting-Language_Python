"""
Assignment 3 - Scripting Language / Python
Author: Bruno Lopes
Date: 11 Oct 2023

Question 2: Given a list from a to e, iterate through the list, and count the occurrence 
of each element, and create a dictionary to show the count of each element.
Ex:
sampleList = ['a', 'c', 'b', 'd', 'd', 'a', 'e', 'a', 'e']
Expected Outcome: dict = {'a': 3, 'c': 1, 'b': 1, 'd': 2, 'e': 2}

"""

list = ['a', 'c', 'b', 'd', 'd', 'a', 'e', 'a', 'e']
## dictionary with the count of each element
countElements = {'a':list.count('a'), 'b':list.count('b'), 'c':list.count('c'), 'd':list.count('d'), 'e':list.count('e')}
print(countElements)

