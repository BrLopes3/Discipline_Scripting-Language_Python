"""
Question 1: Accept two int values from user and return their product.
If the product is
greater than 1000, then return their sum

"""
print("Assignment 1: Question 1")
print("========================")
number1 = input("Enter the first number: ")
number1 = int(number1)

number2 = input("Enter the second number: ")
number2 = int(number2)

product = number1 * number2

summ = number1 + number2

if (product <= 1000):
    print(f"The product of {number1} and {number2} is {product}")
else:
    print(f"The sum of {number1} and {number2} is {summ}")
    
        
    
