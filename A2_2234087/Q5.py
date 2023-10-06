"""
Assignment 2
Author: Bruno Lopes
Date: 01/10/23

Question 5: Given an input list removes the element at index 4 and 
add it to the 2nd position and also, at the end of the list

List = [54, 44, 27, 79, 91, 41]

output:
[54, 44, 118, 79, 41, 91]

"""
list = [54, 44, 27, 79, 91, 41]

list[2] = list[2]+list[4]
list.append(list[4])
list.remove(list[4])

print(list)