"""
Assignment 3 - Scripting Language / Python
Author: Bruno Lopes
Date: 12 Oct 2023

Question 9: Given a list iterate it and count the occurrence of each element and create a
dictionary to show the count of each element.
For example: list = [10, 20, 30, 10, 20, 40, 50]
Expected Outcome: dict = {10: 2, 20: 2, 30: 1, 40: 1, 50: 1}

"""
# Create a list
list = [10, 20, 30, 10, 20, 40, 50]
print("List: ", list)

# Create a dictionary
dict = {}

# Loop through the list
for i in list:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

print("Outcome: dict = ", dict)

