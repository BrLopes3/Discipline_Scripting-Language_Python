"""
Assignment 3 - Scripting Language / Python
Author: Bruno Lopes
Date: 11 Oct 2023

Question 1: Given a list slice it into three chunks, (the last one could be 
equal with others) and then display in normal order and reverse order.
"""

mainList = input("Enter a list with elements separated by space: ").split()
print("The list is: ", mainList)

## slice the list into 3 chunks
## list of chunks  = [chunk1, chunk2, chunk3]
if (len(mainList)<3):
    print("The list is too short to be sliced into 3 chunks")
else:
    if (len(mainList)%3 ==0):
        chunkSize1 = len(mainList)/3
        chunkSize2 = chunkSize1

        chunk1 = mainList[:chunkSize1]
        chunk2 = mainList[chunkSize1:chunkSize1+chunkSize2]
        chunk3 = mainList[chunkSize1+chunkSize2:]

    elif(len(mainList)%3 ==1):
        chunkSize1 = int(len(mainList)/3)
        chunkSize2 = chunkSize1

        chunk1 = mainList[:chunkSize1]
        chunk2 = mainList[chunkSize1:chunkSize1+chunkSize2]
        chunk3 = mainList[chunkSize1+chunkSize2:]

    else:
        chunkSize1 = int(len(mainList)/3)
        chunkSize2 = chunkSize1 + 1

        chunk1 = mainList[:chunkSize1]
        chunk2 = mainList[chunkSize1:chunkSize1+chunkSize2]
        chunk3 = mainList[chunkSize1+chunkSize2:]

print("dividing the list into 3 chunks we have:")
print(chunk1)
print(chunk2)
print(chunk3)

print("reversing the order of the chunks we have:")
print(chunk1[::-1])
print(chunk2[::-1])
print(chunk3[::-1])

print("The main list in reverse order is:")
print(mainList[::-1])
