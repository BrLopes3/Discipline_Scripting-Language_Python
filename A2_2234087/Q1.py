"""
Assignment 2
Author: Bruno Lopes
Date: 30/09/23

Question 1: arrange String characters such that lowercase letters should come first
Given input String of combination of the lower and upper case arrange characters in such a way
that all lowercase letters should come first.

Example:
Input: "PyNaTive" Output: " aeivyNPT "

"""

stringInput = input("Enter with a string: ")
arrayString = []
arrayString.extend(stringInput)

for i in arrayString:
    if i.isupper():
        arrayString.append(i)
        arrayString.remove(i)

finalString =''.join(arrayString)

print(finalString)
