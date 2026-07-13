# Student Grade Calculator
'''Problem Statement 1: Student Grade Calculator
Write a Python program that defines a function calculate_grade(marks).
The function should:
•
Accept marks (0–100) as a parameter.
•
Return the grade according to the following criteria:
o
90 and above → A+
o
75–89 → A
o
60–74 → B
o
40–59 → C
o
Below 40 → Fail
The main program should:
•
Accept marks of 5 students.
•
Call the function for each student.
•
Display the marks and corresponding grade.'''
#-----------------------------------coding----------------------------------------------
# Function to calculate grade based on marks
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"

# Main program
students = {}

# Accept marks of 5 students
for i in range(1, 6):
    name = input(f"Enter name of student {i}: ")
    marks = int(input(f"Enter marks of {name} (0-100): "))
    grade = calculate_grade(marks)
    students[name] = {"Marks": marks, "Grade": grade}

# Display marks and corresponding grade
print("\nStudent Report:")
for name, info in students.items():
    print(f"{name}: Marks = {info['Marks']}, Grade = {info['Grade']}")
#---------------------------------------------------------------------------------
'''output:
Enter name of student 1: Aman
Enter marks of Aman (0-100): 95
Enter name of student 2: Riya
Enter marks of Riya (0-100): 85
Enter name of student 3: Karan
Enter marks of Karan (0-100): 70
Enter name of student 4: Sneha
Enter marks of Sneha (0-100): 55
Enter name of student 5: Vikram
Enter marks of Vikram (0-100): 35

Student Report:
Aman: Marks = 95, Grade = A+
Riya: Marks = 85, Grade = A
Karan: Marks = 70, Grade = B
Sneha: Marks = 55, Grade = C
Vikram: Marks = 35, Grade = Fail
'''