"""
Assignment 2
Author: Bruno Lopes
Date: 01/10/23

Question 6: Write a Python program to reverse a given string
Example:
Input: "python"
Output: "nohtyp"

"""
stringInput1 = input("Enter the string: ")
arraysString = []
arraysString.extend(stringInput1)
arraysString.reverse()
string2 = ''.join(arraysString)
print(string2)
