
"""
COMP-2040 - Assignment 6a

This code is about: Working With TXT Files
    
Created on Tue Feb  6 15:29:16 2024

@author: Mariah Quinquito
"""

#Modifies the specified text file by replacing the word in the line.
def modify_file(file_path):
    updated_lines = []

    # Read the original file and modify the lines
    with open(file_path, 'r') as file:
        for line in file:
            if 'Aqua' in line:
                updated_lines.append('Azure #007fff\n')
            else:
                updated_lines.append(line)

    # Write the modified content back to the original file
    with open(file_path, 'w') as file:
        file.writelines(updated_lines)

file_path = ('C:/Users/AJ/OneDrive/Desktop/Python/Assignment'
             '/Assignment 6a/colors.txt')

modify_file(file_path)
print("TXT file updated successfully.")

