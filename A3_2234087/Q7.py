"""
Assignment 3 - Scripting Language / Python
Author: Bruno Lopes
Date: 12 Oct 2023

Question 7: Remove duplicate from a list and create a tuple and find the minimum and
maximum number.
sampleList = [87, 45, 41, 65, 94, 41, 99, 94]
"""
sampleList = [87, 45, 41, 65, 94, 41, 99, 94]
print("Original list: ", sampleList)

# Remove duplicates
uniqueList = [] ##empty list
"""
for i in sampleList:
    if i not in uniqueList:
        uniqueList.append(i)

to avoid using this comparisons we can use set() function
to define a list of unique values
"""

uniqueList = list(set(sampleList))

print("Unique list: ", uniqueList)

# Create a tuple
tupleList = tuple(uniqueList)
print("Tuple list: ", tupleList)

# Find the minimum and maximum number

print("Minimum number: ", min(tupleList))
print("Maximum number: ", max(tupleList))

