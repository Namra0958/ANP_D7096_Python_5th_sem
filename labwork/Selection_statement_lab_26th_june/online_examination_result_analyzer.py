#Online Examination Result Analyzer
'''Problem Statement
A student appears in 5 subjects.
Rules:
•
Minimum 40 marks in every subject to pass.
•
Distinction → Average ≥ 75
•
First Division→ Average ≥ 60
•
Second Division → Average ≥ 50
•
Pass → Average ≥ 40
•
Fail if any subject score < 40
--------------------------------------------------------------------------------
Sample Input
Hindi : 85 English : 78 Mathematics : 82 Science : 75 Computer : 90
-------------------------------------------------------------------------------
Sample Output
Average Marks: 82.0 Result: PASS Classification: Distinctio
#-------------------------------------------------------------------------------'''
#-------------------------------coding---------------------------------------------------
# WAP for Online Examination Result Analyzer with Validation

try:
    hindi = float(input("Enter Hindi Marks: "))
    english = float(input("Enter English Marks: "))
    maths = float(input("Enter Mathematics Marks: "))
    science = float(input("Enter Science Marks: "))
    computer = float(input("Enter Computer Marks: "))

    # Validation
    marks = [hindi, english, maths, science, computer]

    if any(m < 0 or m > 100 for m in marks):
        print("Invalid Input! Marks must be between 0 and 100.")

    else:
        average = sum(marks) / 5

        # Check Pass/Fail
        if any(m < 40 for m in marks):
            print("Average Marks:", average)
            print("Result: FAIL")

        else:
            print("Average Marks:", average)
            print("Result: PASS")

            # Classification
            if average >= 75:
                classification = "Distinction"
            elif average >= 60:
                classification = "First Division"
            elif average >= 50:
                classification = "Second Division"
            else:
                classification = "Pass"

            print("Classification:", classification)

except ValueError:
    print("Invalid Input! Please enter numeric values only.")
#---------------------------------------------------------------------------
'''output:
Hindi : 85
English : 78
Mathematics : 82
Science : 75
Computer : 90
Average Marks: 82.0
Result: PASS
Classification: Distinction'''