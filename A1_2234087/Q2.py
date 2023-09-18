"""
Question 2: Accept five int values from user and return their average.

"""
print("Assignment 1: Question 2")
print("========================")
print("Enter the 5 integers to calculate the average:")

listOfNumbers = []

for i in range(5):
    num = int(input(f"Number {i+1}: "))
    listOfNumbers.append(num)

average = sum(listOfNumbers) / len(listOfNumbers)

print(f"The average of the numbers is: {average}")
