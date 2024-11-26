import time
import math
import string

"""
COMP-2040 - Assignment 2

This code is about: checking if the current minute is even or odd, 
skipping every second letter of the alphabet, and calculating the 
variance and standard deviation of a list of numbers.

@Author: Mariah Anjannelle A. Quinquito
@Date: 04-01-2024

"""

# 1 If current minute is even or odd
for minute in range(2):
    current_minute = int(time.strftime("%M"))
    if current_minute % 2 == 0:
        print(f"The current minute ({current_minute}) is even.\n")
    else:
        print(f"The current minute ({current_minute}) is odd.\n")
#    time.sleep(60)
    
# 2 skipping every second letter of the alphabet
reversed_alphabet = string.ascii_lowercase[::-1]
for alphabet in range(0, len(reversed_alphabet), 2):
    print(reversed_alphabet[alphabet])

# 3 calculate the variance and standard deviation of the list
numbers = [73.79693173, 41.76429734, 53.66368384, 24.60911367, 73.60414637, 
           62.26858213, 13.9670495, 70.97809816, 17.9978692, 56.10505197]

mean = sum(numbers) / len(numbers)

squared_number = []
for number in numbers:
    difference = (number - mean) ** 2
    squared_number.append(difference)

variance = sum(squared_number) / len(numbers)

std_deviation = math.sqrt(variance)

print(f"\nPopulation Variance: {variance}")
print(f"Population Standard Deviation: {std_deviation}")