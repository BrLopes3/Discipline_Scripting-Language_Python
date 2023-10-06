"""
Assignment 2
Author: Bruno Lopes
Date: 03/10/23

Question 8:Write a Python program to display astrological sign for given date of birth.
Expected Output:
Input birthday: 15
Input month of birth (e.g. march, july etc): may Your Astrological sign is : Taurus

"""

dayOfBirth = int(input("Input day of birthday: "))
monthOfBirth = input("Input month of birth (e.g. march, july etc): ")

def defineSign(dayOfBirth, monthOfBirth):

    if monthOfBirth == "december":
        astrologicalSign = 'Sagittarius' if (dayOfBirth < 22) else 'Capricorn'
    elif monthOfBirth == "january":
        astrologicalSign = 'Capricorn' if (dayOfBirth < 20) else 'Aquarius'
    elif monthOfBirth == "february":
        astrologicalSign = 'Aquarius' if (dayOfBirth < 19) else 'Pisces'
    elif monthOfBirth == "march":
        astrologicalSign = 'Pisces' if (dayOfBirth < 21) else 'Aries'
    elif monthOfBirth == "april":
        astrologicalSign = 'Aries' if (dayOfBirth < 20) else 'Taurus'
    elif monthOfBirth == "may":
        astrologicalSign = 'Taurus' if (dayOfBirth < 21) else 'Gemini'
    elif monthOfBirth == "june":
        astrologicalSign = 'Gemini' if (dayOfBirth < 21) else 'Cancer'
    elif monthOfBirth == "july":
        astrologicalSign = 'Cancer' if (dayOfBirth < 23) else 'Leo'
    elif monthOfBirth == "august":
        astrologicalSign = 'Leo' if (dayOfBirth < 23) else 'Virgo'
    elif monthOfBirth == "september":
        astrologicalSign = 'Virgo' if (dayOfBirth < 23) else 'Libra'
    elif monthOfBirth == "october":
        astrologicalSign = 'Libra' if (dayOfBirth < 23) else 'Scorpio'
    elif monthOfBirth == "november":
        astrologicalSign = 'scorpio' if (dayOfBirth < 22) else 'Sagittarius'
    
    print(f"The Astrological Sign is {astrologicalSign}")



defineSign(dayOfBirth, monthOfBirth.lower())

