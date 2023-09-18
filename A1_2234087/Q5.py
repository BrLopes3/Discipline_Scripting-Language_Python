"""
Question 5: Given a list of ints, return True if first and last number of a list is same

"""
print("Assignment 1: Question 5")
print("========================")

listOfNumbers1 = [1, 2, 3, 4, 5, 2]
print(f"The List 1 is: {listOfNumbers1}")
listOfNumbers2 = [1, 2, 3, 4, 5, 1]
print(f"The List 2 is: {listOfNumbers2}")

listOfNumbers = listOfNumbers1

if listOfNumbers[0] == listOfNumbers[len(listOfNumbers)-1]:
    print(f"List 1 analysis: {True}, the first and last numbers are same")
else:
    print(f"List 1 analysis: {False}, the first and last numbers are NOT the same")

listOfNumbers = listOfNumbers2

if listOfNumbers[0] == listOfNumbers[len(listOfNumbers)-1]:
    print(f"List 2 analysis: {True}, the first and last numbers are same")
else:
    print(f"List 2 analysis: {False}, the first and last numbers are NOT the same")
