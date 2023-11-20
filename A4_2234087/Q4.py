"""
Assignment 4
Date: 2023 - 10 - 28
Author: Bruno Lopes

Question 4: Implement a python program to check if a number is an Armstrong number
by using lambda, map, and filter.
An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is
equal to the number itself. For example, 371 is an Armstrong number since 3**3 + 7**3 + 1**3
= 371.

References: https://pages.mtu.edu/~shene/COURSES/cs201/NOTES/chap04/arms.html
Used only for the definition of Armstrong number and examples of armstrong numbers
for testing in this code.

"""
def armstrong(n):
##to divide the digits we can transform n in an array
    n = int(n)
    m = str(n)
    a = []
    ##before append the characters in the array we need to convert them to int
    for char in m:
        num = int(char)
        a.append(num)
    print(a)

    ##test if the number is an Armstrong number
    ##first step - cube the numbers
    for i in range(len(a)):
        a[i] = a[i]**3
    ##second step - sum the numbers
    import functools
    result = functools.reduce(lambda x,y:x+y, a)
    print(result)
    ##third step - test if the result is equal to the number
    if result == n:
        resultText = "The number is an Armstrong number"
    else:
        resultText = "The number is not an Armstrong number"
    
    return resultText


n = input("Please enter a number for verificaton: ")
print(armstrong(n))
