"""
Assignment 2
Author: Bruno Lopes
Date: 01/10/23

Question 7:

"""
for i in range(1, 10):
    if i<=5:
        for j in range(1, 6):
            if(j<=i):
                print("*", end=" ")
    else:
        for j in range(1, 6):
            if(j<=10-i):
                print("*", end=" ")
    print()

