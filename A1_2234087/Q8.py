"""
Question 8: Given a two list. Create a third list by picking an odd-index element from the
first list and even index elements from second.
"""
print("Assignment 1: Question 8")
print("========================")

listOne = [3, 6, 9, 12, 15, 18, 21]
print(f"List 1: {listOne}")

listTwo = [4, 8, 12, 16, 20, 24, 28]
print(f"List 2: {listTwo}")

listThree = []
for i in range(1, len(listOne),1):
    if(i % 2 != 0):
        listThree.append(listOne[i])
    else:
        listThree.append(listTwo[i])

print(f"List 3: {listThree}")
