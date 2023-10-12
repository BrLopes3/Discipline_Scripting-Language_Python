"""
Assignment 3 - Scripting Language / Python
Author: Bruno Lopes
Date: 11 Oct 2023

Question 4: Given two sets, checks if One Set is Subset or superset of Another Set. if the
subset is found delete all elements from that set
firstSet = {27, 43, 34}
secondSet = {34, 93, 22, 27, 43, 53, 48}

"""

firstSet = {27, 43, 34, 80, 99}
secondSet = {34, 93, 22, 27, 43, 53, 48, 80, 99}
thirdSet = {34, 93, 22, 27, 43, 53, 48, 66}

result1 = firstSet.issubset(secondSet)
result2 = thirdSet.issubset(secondSet)

## testing if firstSet is subset of secondSet
if result1 == True:
    print("First set is subset of second set")
    firstSet.clear()
    print(firstSet)
else:
    print("First set is not subset of second set")

## testing if thirdSet is subset of secondSet
if result2 == True:
    print("Third set is subset of second set")
    thirdSet.clear()
    print(thirdSet)
else:
    print("Third set is not subset of second set")