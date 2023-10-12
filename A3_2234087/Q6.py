"""
Assignment 3 - Scripting Language / Python
Author: Bruno Lopes
Date: 12 Oct 2023

Question 6: Given a dictionary get all values from the dictionary and add it in a list but
don’t add duplicates.

speed ={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}

"""

speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
speedList = []

for value in speed.values():
    if value not in speedList:
        speedList.append(value)

print("list without duplicates",speedList)