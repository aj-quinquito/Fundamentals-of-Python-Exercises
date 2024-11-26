"""
COMP-2040 - Assignment 4 - Question 2

This code is about: creates and prints a dictionary of character frequencies 
for a user-input string in alphabetical order of the keys.

@Author: Mariah Anjannelle A. Quinquito
@Date: 26-01-2024

"""

user_input = input("Enter a string: ")

char_frequency = {}
for char in user_input:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

sorted_char_frequency = dict(sorted(char_frequency.items()))

print("Character frequencies:")

for char, frequency in sorted_char_frequency.items():
    print(f"{char}: {frequency}")
