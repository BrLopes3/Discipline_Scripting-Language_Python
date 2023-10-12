"""
Question 7: Find all occurrences of “USA” in given string (uppercase and lowercase).
"""
print("Assignment 1: Question 7")
print("========================")

sentence = "Welcome to USA. usa awesome, isn't it?"

print(f"Sentence: {sentence}")

numberOfUSA = sentence.count("USA") + sentence.count("usa")

print(f"The sentence has {numberOfUSA} occurrences of USA/usa.")


