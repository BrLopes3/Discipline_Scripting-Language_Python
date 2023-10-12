"""
Question 4: Given a string and an int n, remove characters from string starting from zero
upto n and return a new string

"""
print("Assignment 1: Question 4")
print("========================")
stringInput = input("Enter a string: ")
n = int(input("Enter an integer: "))
newString = stringInput[n+1:]
print(f"The new string created removing characters from 0 to {n} of the original string is: {newString}")
