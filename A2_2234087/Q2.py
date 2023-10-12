"""
Assignment 2
Author: Bruno Lopes
Date: 30/09/23

Question 2: Given an input string Count all lower case, upper case, digits, and special
symbols

"""
stringInput = input("Enter with a string: ")
arrayString = []
arrayString.extend(stringInput)

lowerCaseNumbers = 0
upperCaseNumbers = 0
digitsNumbers = 0
specialSymbolsNumbers = 0

for i in arrayString:
    if i.islower():
        lowerCaseNumbers += 1
    elif i.isupper():
        upperCaseNumbers += 1
    elif i.isdigit():
        digitsNumbers += 1
    else:
        specialSymbolsNumbers += 1

print("Ocurrencies of lower cases: ", lowerCaseNumbers,"\nOcurrencies of UPPER CASES: ", upperCaseNumbers
,"\nDigits numbers: ", digitsNumbers,"\nOcurrencies of Special symbols: ", specialSymbolsNumbers)





