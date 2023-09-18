"""
Assignment 01
Date: 2023-09-17
Author: Bruno Lopes

"""

print("Assignment 1: Scripting Language")
print("================================")
print("Chose a number to define the question you want to execute:")
print("1 - Question 1\n2 - Question 2\n3 - Question 3\n4 - Question 4\n5 - Question 5\n6 - Question 6\n7 - Question 7\n8 - Question 8\n9 - Question 9\n")

def question1():
    
    print("Assignment 1: Question 1")
    print("========================")
    number1 = input("Enter the first number: ")
    number1 = int(number1)

    number2 = input("Enter the second number: ")
    number2 = int(number2)

    product = number1 * number2

    summ = number1 + number2

    if product <= 1000:
     print(f"The product of {number1} and {number2} is {product}")
    else:
     print(f"The sum of {number1} and {number2} is {summ}")

def question2():
    print("Assignment 1: Question 2")
    print("========================")
    print("Enter the 5 integers to calculate the average:")

    listOfNumbers = []

    for i in range(5):
        num = int(input(f"Number {i+1}: "))
        listOfNumbers.append(num)

    average = sum(listOfNumbers) / len(listOfNumbers)

    print(f"The average of the numbers is: {average}")

def question3():
    print("Assignment 1: Question 3")
    print("========================")
    stringInput = input("Enter a string of odd length greater than 7: ")
    if (len(stringInput) > 7) and (len(stringInput) % 2 != 0):
        middle = len(stringInput) // 2
        print(f"a string made of the middle three chars of this String: {stringInput[middle-1:middle+2]}")
    else:
        print("Invalid input")

def question4():
    print("Assignment 1: Question 4")
    print("========================")
    stringInput = input("Enter a string: ")
    n = int(input("Enter an integer: "))
    newString = stringInput[n+1:]
    print(f"The new string created removing characters from 0 to {n} of the original string is: {newString}")

def question5():
    print("Assignment 1: Question 5")
    print("========================")

    listOfNumbers1 = [1, 2, 3, 4, 5, 2]
    print(f"The List 1 is: {listOfNumbers1}")
    listOfNumbers2 = [1, 2, 3, 4, 5, 1]
    print(f"The List 2 is: {listOfNumbers2}")

    listOfNumbers = listOfNumbers1

    if listOfNumbers[0] == listOfNumbers[len(listOfNumbers)-1]:
        print(f"List 1 analysis: {True}, the first and last numbers are same")
    else:
        print(f"List 1 analysis: {False}, the first and last numbers are NOT the same")

    listOfNumbers = listOfNumbers2

    if listOfNumbers[0] == listOfNumbers[len(listOfNumbers)-1]:
        print(f"List 2 analysis: {True}, the first and last numbers are same")
    else:
        print(f"List 2 analysis: {False}, the first and last numbers are NOT the same")

def question6():
    print("Assignment 1: Question 6")
    print("========================")

    string1 = input("Enter the first string: ")

    string2 = input("Enter the second string: ")

    middle = len(string1) // 2

    newString = string1[:int(middle)] + string2 + string1[int(middle):]

    print(f"The new string created with the composition of {string1} and {string2} is: {newString}")

def question7():
    print("Assignment 1: Question 7")
    print("========================")

    sentence = "Welcome to USA. usa awesome, isn't it?"

    print(f"Sentence: {sentence}")

    numberOfUSA = sentence.count("USA") + sentence.count("usa")

    print(f"The sentence has {numberOfUSA} occurrences of USA/usa.")

def question8():
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
    print("List created with the odd index of List 1 and even index of List 2: ")
    print(f"List 3: {listThree}")

def question9():
    print("Assignment 1: Question 9")
    print("========================")

    list = [54, 44, 27, 79, 91, 41]

    print(f"List: {list}\n")

    list.insert(2, list.pop(4))

    print(f"List removing the element in index 4 and inserting it at the 2nd position:\n{list}\n")

    list.append(list[2])

    print(f"List adding the element at the 2nd position also at the end:\n{list}\n")


question = int(input("Option: "))

def menu(question):
    if question == 1:
        question1()
    elif question == 2:
        question2()
    elif question == 3:
        question3()
    elif question == 4:
        question4()
    elif question == 5:
        question5()
    elif question == 6:
        question6()
    elif question == 7:
        question7()
    elif question == 8:
        question8()
    elif question == 9:
        question9()
    else:
        print("Invalid option. Please try again.")

menu(question)
