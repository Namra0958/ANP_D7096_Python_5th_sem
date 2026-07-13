#List Analysis using Functions
'''Write a Python program that defines the following functions:
•
find_max(numbers)
•
find_min(numbers)
•
find_average(numbers)
The program should:
•
Accept a list of 10 integers from the user.
•
Call all three functions.
•
Display the maximum value, minimum value, and average of the list.'''
#------------------------------coding----------------------------------------------
# Function to find maximum value
def find_max(numbers):
    return max(numbers)

# Function to find minimum value
def find_min(numbers):
    return min(numbers)

# Function to find average value
def find_average(numbers):
    return sum(numbers) / len(numbers)

# Main program
numbers = []

# Accept a list of 10 integers from the user
print("Enter 10 integers:")
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Call all three functions
maximum = find_max(numbers)
minimum = find_min(numbers)
average = find_average(numbers)

# Display results
print("\nList Analysis Results:")
print(f"Maximum value: {maximum}")
print(f"Minimum value: {minimum}")
print(f"Average value: {average:.2f}")
#-------------------------------------------------------------------------------------
'''output:
Enter 10 integers: 1 2 3 4 5 6 7 8 9 10

List Analysis Results:
Maximum value: 10
Minimum value: 1
Average value: 5.50
'''