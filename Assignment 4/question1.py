"""
COMP-2040 - Assignment 4 - Question 1

This code is about: sorts five user-input integers from smallest to 
largest without using the sort() method

@Author: Mariah Anjannelle A. Quinquito
@Date: 26-01-2024

"""
# Get five valid integers from the user
integer_list = []
for each_input in range(5):
    while True:
        user_input = input("Enter an integer: ")
        try:
            valid_integer = int(user_input)
            integer_list.append(valid_integer)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

original_list = list(integer_list)

# Sorting the list without using sort() method
for current_index in range(len(integer_list)):
    for next_index in range(current_index + 1, len(integer_list)):
        if integer_list[current_index] > integer_list[next_index]:
            integer_list[current_index], integer_list[next_index] = ( 
                integer_list[next_index], integer_list[current_index] )


print(f"Original list: {original_list}")
print(f"Sorted list: {integer_list}")
