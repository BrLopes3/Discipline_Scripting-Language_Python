"""
Assignment 2
Author: Bruno Lopes
Date: 01/10/23

Question 4: Given a two list. Create a third list by picking an odd-index 
element from the first list and even index elements from second.

listOne = [*3, *6, 9, *12, 15, *18, 21]
listTwo = [4, 8, *12, 16, *20, 24, *28]

output:
listThree = [3, 6, 12, 12, 20, 18, 28]

"""

listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
listThree = []

i=0
while i < len(listOne):
    if i==0:
        listThree.append(listOne[i])
    elif i%2 == 0:
        listThree.append(listTwo[i])
    else:
        listThree.append(listOne[i])
    i += 1

print(listThree)
