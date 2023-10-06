"""
Assignment 2
Author: Bruno Lopes
Date: 01/10/23

Question 3: String characters balance Test
We’ll say that a String s1 and s2 is balanced if all the chars in the string1 
are there in s2. characters position doesn’t matter.

Example:
s1 = "yn" s2 = "Pynative" 
Output: s1 and s2 are balanced True

s1 = "ynf" s2 = "Pynative" 
Output: s1 and s2 are balanced False

"""
stringInput1 = input("Enter with the first string: ")

stringInput2 = input("Enter with the second string: ")

if stringInput2.find(stringInput1) == True:
    print("s1 and s2 are balanced True")
else:
    print("s1 and s2 are balanced False")