#Vowel Counter using Function
'''Write a Python program that defines a function count_vowels(text).
The function should:
•
Accept a string.
•
Count the total number of vowels (a, e, i, o, u) irrespective of case.
•
Return the total vowel count.
The main program should:
•
Accept a sentence from the user.
•
Call the function.
•
Display the total number of vowels.
Sample Output
Enter a sentence: Python Programming is Fun Total Vowels: 6'''
#-----------------------------------coding----------------------------------------------
# Function to count vowels in a string
def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text.lower():   # convert to lowercase for case-insensitive check
        if char in vowels:
            count += 1
    return count

# Main program
sentence = input("Enter a sentence: ")

# Call the function
vowel_count = count_vowels(sentence)

# Display the result
print(f"Total Vowels: {vowel_count}")
#-------------------------------------------------------------------------------------------
'''output:
Enter a sentence: Python Programming is Fun
Total Vowels: 6
'''