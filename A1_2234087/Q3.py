"""
Question 3: Given a string of odd length greater 7, return a string made of the middle three
chars of a given String
"""
print("Assignment 1: Question 3")
print("========================")
stringInput = input("Enter a string of odd length greater than 7: ")
if (len(stringInput) > 7) and (len(stringInput) % 2 != 0):
    middle = len(stringInput) // 2
    print(f"a string made of the middle three chars of this String: {stringInput[middle-1:middle+2]}")
else:
    print("Invalid input")
