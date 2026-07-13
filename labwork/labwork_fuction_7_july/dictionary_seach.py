#Dictionary Search System
'''Write a Python program that defines a function search_student(student_dict, roll_no).
The function should:
•
Accept a dictionary where:
o
Key = Roll Number
o
Value = Student Name
•
Search for the given roll number.
•
Return the student name if found; otherwise return "Student Not Found".
The main program should:
•
Create a dictionary of at least 5 students.
•
Accept a roll number from the user.
•
Display the search result.'''
#-----------------------------------coding----------------------------------------------
# Function to search for a student by roll number
def search_student(student_dict, roll_no):
    if roll_no in student_dict:
        return student_dict[roll_no]
    else:
        return "Student Not Found"

# Main program
students = {
    101: "Rahul",
    102: "Priya",
    103: "Ankit",
    104: "Sneha",
    105: "Vikram"
}

# Accept roll number from user
roll_no = int(input("Enter Roll Number to search: "))

# Call the function and display result
result = search_student(students, roll_no)
print(f"Search Result: {result}")
#-------------------------------------------------------------------------------------
'''output:
Enter Roll Number to search: 103
Search Result: Ankit
'''