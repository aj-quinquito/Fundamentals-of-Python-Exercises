"""
COMP-2040 - Assignment 3 - Palindrome Checker

This code is about: checking if a word entered by the user is a palindrome 
(spelled the same way backward and forward)

@Author: Mariah Anjannelle A. Quinquito
@Date: 18-01-2024

"""

def is_palindrome(word):
    """check if word is palindrome"""
    palindrome_word = word.lower()
    return palindrome_word == palindrome_word[::-1]

def user_enter_word():
    return input("Enter a word: ")

user_input = user_enter_word()
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")