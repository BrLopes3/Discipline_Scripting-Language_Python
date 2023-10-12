"""
Question 6: Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1

"""
print("Assignment 1: Question 6")
print("========================")

string1 = input("Enter the first string: ")

string2 = input("Enter the second string: ")

middle = len(string1) // 2

newString = string1[:int(middle)] + string2 + string1[int(middle):]

print(f"The new string created with the composition of {string1} and {string2} is: {newString}")