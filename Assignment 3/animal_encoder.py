"""
COMP-2040 - Assignment 3 - Animal Encoder

This code is about: checking a dictionary with specific key-value pairs 
representing animals and their corresponding codes.

@Author: Mariah Anjannelle A. Quinquito
@Date: 18-01-2024

"""

animal_dictionary = {'dog': 0, 'cat': 1, 'frog': 2}

"""def mapping_an_animal(animal):
    return animal_dictionary.get(animal)"""

input_animal = []
for each_animal in range(5):
    user_input = input("\nEnter an animal (dog, cat, or frog): ").lower()
    
    while user_input not in animal_dictionary:
        print("Invalid input. Please enter a valid animal.\n")
        user_input = input("Enter an animal (dog, cat, or frog): ").lower()

    input_animal.append(user_input)

encoded_labels = [animal_dictionary[each_animal]
                  for each_animal in input_animal]

print(f"\nLabels: {input_animal}")
print(f"Encoded Labels: {encoded_labels}")

