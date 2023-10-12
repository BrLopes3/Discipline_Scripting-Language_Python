"""
Assignment 3 - Scripting Language / Python
Author: Bruno Lopes
Date: 11 Oct 2023

Question 5: Iterate a given list and check if a given element already exists in a dictionary as
a keys value, display the output as a set and if not delete it from the set.

rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict ={'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

"""

rollNumber = [47, 64, 69, 37, 76, 83, 95, 97] ##list
sampleDict ={'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97} ##dictionary
setResult = set() ##define an empty set
for i in rollNumber:
    if i in sampleDict.values():
        print(i, "is in the dictionary")
        setResult.add(i)
    else:
        print(i, "is not in the dictionary")
        rollNumber.remove(i)

print("the final list becomes: ", rollNumber, type(rollNumber))
print("the set is: ", setResult, type(setResult))

