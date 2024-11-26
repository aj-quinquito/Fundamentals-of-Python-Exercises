import csv
"""
COMP-2040 - Assignment 6b

This code is about: Working With CSV Files

Created on Tue Feb  6 15:46:08 2024

@author: Mariah Quinquito
"""

data = [
    {"Temp": 1.1, "Press": 55.5, "Humidity": 22.2},
    {"Temp": 3.3, "Press": 4.4, "Humidity": 6.6},
    {"Temp": 8.8, "Press": 99.9, "Humidity": 7.7}
]

file_path = ('C:/Users/AJ/OneDrive/Desktop/Python/Assignment'
             '/Assignment 6b/weather.csv')

# Write data to CSV file
with open(file_path, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["Temp", "Press", "Humidity"])
    writer.writeheader()
    writer.writerows(data)

print("CSV file created successfully.")


def read_and_calculate_average(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    # Check if the data is not empty
    if data:
        # Print the data
        print("\nData from CSV file:")
        for row in data:
            print(row)

        # Calculate the average temperature
        temperatures = [float(row["Temp"]) for row in data]
        average_temperature = sum(temperatures) / len(temperatures)

        # Print the average temperature
        print(f"\nAverage Temperature: {average_temperature:.2f}")
    else:
        print("CSV file is empty.")


# Call the function with the file path
read_and_calculate_average(file_path)
