"""
Question 9: Given an input list removes the element at index 4 and add it to the 2nd
position and also, at the end of the list

"""
print("Assignment 1: Question 9")
print("========================")

list = [54, 44, 27, 79, 91, 41]

print(f"List: {list}\n")

list.insert(2, list.pop(4))

print(f"List removing the element in index 4 and inserting it at the 2nd position:\n{list}\n")

list.append(list[2])

print(f"List adding the element at the 2nd position also at the end:\n{list}\n")
