"""
Assignment 3 - Scripting Language / Python
Author: Bruno Lopes
Date: 12 Oct 2023

Question 8: Given an input string, count occurrences of
all characters within a string
Example:

Input: "pynativepynvepynative"
Output: {'p': 3, 'y': 3, 'n': 3, 'a': 2, 't': 2, 'i': 2, 'v': 3, 'e': 3}
"""

inputString = "pynativepynvepynative"
print("Input string: ", inputString)
# Create a dictionary
dict = {}

# Loop through the string
for i in inputString:
    # Check if the character is in the dictionary
    if i in dict:
        # If it is, add 1 to the value
        dict[i] += 1
    else:
        # If it is not, add the character to the dictionary for the first time
        dict[i] = 1

print("Output: ")
print(dict)
