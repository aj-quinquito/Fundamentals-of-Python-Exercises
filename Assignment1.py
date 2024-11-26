"""
COMP-2040 - Assignment 1

This program is to perform basic arithmetic operations on a list of integers 
without relying on built-in functions.

@Author: Mariah Anjannelle A. Quinquito
@Date: 01-04-2024

"""
# input list
"""numbers = []
while True:
    try:
        num = input("Enter a number (press Enter twice to finish): \n")
        
        if num == "":
            break  
        else:
            numbers.append(int(num))
    except ValueError:
        print("Invalid input! Please enter a valid number.\n")"""

# list
numbers = [5, 0, -10, 4, 9, -5, 13, 26, -17, 18]

# Print out each number in the list.
for int in numbers:   
    print(int)
    
# Calculate the sum
total_sum = 0
for int in numbers:
    total_sum += int

print(f"\nSum: {total_sum}")

# Calculate the average
if not numbers:
    average = 0 
else:
    average = total_sum / len(numbers)
print(f"\nAverage: {average}")


# Finding the largest number
if not numbers:
    max_number = 0
else:
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num

print(f"\nLargest number: {max_number}")
