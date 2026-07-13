#Student Subject Report Card
'''Problem Statement: Create a nested dictionary to store marks of students in three subjects.
Example:
{ 'Rahul': {'Math': 85, 'Science': 90, 'English': 88},
'Priya': {'Math': 78, 'Science': 95, 'English': 82}, 'Ankit': {'Math': 91, 'Science': 89, 'English': 94} }
Write a program to:
•
Calculate the total marks of each student.
•
Calculate the average marks of each student.
•
Display the topper based on total marks.
•
Display the subject-wise highest marks along with the student's name.
•
Display students whose average is greater than or equal to 85.'''
#------------------------------------coding---------------------------------------
# Nested dictionary storing marks of students
students = {
    'Rahul': {'Math': 85, 'Science': 90, 'English': 88},
    'Priya': {'Math': 78, 'Science': 95, 'English': 82},
    'Ankit': {'Math': 91, 'Science': 89, 'English': 94}
}

# 1. Calculate total marks of each student
print("Total Marks of Each Student:")
totals = {}
for name, subjects in students.items():
    total = sum(subjects.values())
    totals[name] = total
    print(f"{name}: {total}")

# 2. Calculate average marks of each student
print("\nAverage Marks of Each Student:")
averages = {}
for name, subjects in students.items():
    avg = sum(subjects.values()) / len(subjects)
    averages[name] = avg
    print(f"{name}: {avg:.2f}")

# 3. Display the topper based on total marks
topper = max(totals, key=totals.get)
print(f"\nTopper: {topper} with {totals[topper]} marks")

# 4. Display subject-wise highest marks along with the student's name
print("\nSubject-wise Highest Marks:")
subjects = ['Math', 'Science', 'English']
for subject in subjects:
    highest_student = max(students, key=lambda name: students[name][subject])
    print(f"{subject}: {students[highest_student][subject]} by {highest_student}")

# 5. Display students whose average is >= 85
print("\nStudents with Average >= 85:")
for name, avg in averages.items():
    if avg >= 85:
        print(f"{name}: {avg:.2f}")
#---------------------------------------------------------------------------------------------
'''output:
Total Marks of Each Student:
Rahul: 263
Priya: 255
Ankit: 274

Average Marks of Each Student:
Rahul: 87.67
Priya: 85.00
Ankit: 91.33

Topper: Ankit with 274 marks

Subject-wise Highest Marks:
Math: 91 by Ankit
Science: 95 by Priya
English: 94 by Ankit

Students with Average >= 85:
Rahul: 87.67
Priya: 85.00
Ankit: 91.33'''
