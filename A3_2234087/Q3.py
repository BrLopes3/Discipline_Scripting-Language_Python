"""
Assignment 3 - Scripting Language / Python
Author: Bruno Lopes
Date: 11 Oct 2023

Question 3: Given a two list of equal size create a set such that it shows the element from
both lists in the pair.
"""

list1 = [10, 20, 30.5, 67]
list2 = [21, 34, 44, 88]
set1 = set(zip(list1, list2))

print(set1)
print(type(set1))