#Password Strength Checker
'''Write a function check_password(password) that checks whether a password is strong.
A password is considered Strong if:
•
It contains at least 8 characters.
•
It contains at least one uppercase letter.
•
It contains at least one lowercase letter.
•
It contains at least one digit.
The function should return:
•
"Strong Password" or
•
"Weak Password"
The main program should accept a password from the user and display the result.'''
#-------------------------------------coding--------------------------------------------
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
#---------------------------------------------------------------------------------------------
'''output:
Enter 10 integers: 1 2 3 4 5 6 7 8 9 10

List Analysis Results:
Maximum value: 10
Minimum value: 1
Average value: 5.50
'''