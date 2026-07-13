# Student Marks Management System
'''Problem Statement: Create a dictionary to store the marks of 5 students, where the key is the student's name and the value is their marks.
Perform the following operations:
•
Display all student names and marks.
•
Add a new student with marks.
•
Update the marks of an existing student.
•
Delete a student by name.
•
Display the student who scored the highest marks.'''
#--------------------------------coding-----------------------------------------------
# Initialize an empty dictionary to store student marks 
student_marks = {}
# Create a dictionary to store marks of 5 students
student_marks = {
    "Aman": 85,
    "Riya": 92,
    "Karan": 76,
    "Sneha": 89,
    "Vikram": 95
}

# 1. Display all student names and marks
print("All student marks:")
for name, marks in student_marks.items():
    print(f"{name}: {marks}")

# 2. Add a new student with marks
student_marks["Abhishek"] = 88
print("\nAfter adding a new student:")
print(student_marks)

# 3. Update the marks of an existing student
student_marks["Karan"] = 82
print("\nAfter updating Karan's marks:")
print(student_marks)

# 4. Delete a student by name
del student_marks["Sneha"]
print("\nAfter deleting Sneha:")
print(student_marks)

# 5. Display the student who scored the highest marks
highest_student = max(student_marks, key=student_marks.get)
print(f"\nHighest scorer: {highest_student} with {student_marks[highest_student]} marks")
#--------------------------------------------------------------------------------------------------
'''output:
All student marks:
Aman: 85
Riya: 92
Karan: 76
Sneha: 89
Vikram: 95

After adding a new student:
Aman: 85
Riya: 92
Karan: 76
Sneha: 89
Vikram: 95
Abhishek: 88

After updating Karan's marks:
Aman: 85
Riya: 92
Karan: 82
Sneha: 89
Vikram: 95
Abhishek: 88

After deleting Sneha:
Aman: 85
Riya: 92
Karan: 82
Vikram: 95
Abhishek: 88

Highest scorer: Vikram with 95 marks
'''
