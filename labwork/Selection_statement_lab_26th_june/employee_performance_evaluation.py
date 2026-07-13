#Employee Performance Evaluation
'''Problem Statement
An employee is evaluated using:
•
Project Score
•
Attendance Percentage
•
Client Feedback Score
Rules:
•
Excellent → All scores above 90
•
Good → Scores above 75
•
Average → Scores above 60
•
Poor → Otherwise
Additional Rule:
•
Attendance below 70% cannot receive more than Average rating.
-----------------------------------------------------------------------------------------
Sample Input
Project Score: 95 Attendance: 65 Client Feedback: 92
------------------------------------------------------------------------------------------
Sample Output
Performance Rating: Average Reason: Attendance below 70%
-----------------------------------------------------------------------------------------'''
#------------------------------------------coding---------------------------------------------
# WAP to Evaluate Employee Performance with Validation

try:
    project_score = int(input("Enter Project Score: "))
    attendance = int(input("Enter Attendance Percentage: "))
    client_feedback = int(input("Enter Client Feedback Score: "))

    # Validation
    if (project_score < 0 or project_score > 100 or
        attendance < 0 or attendance > 100 or
        client_feedback < 0 or client_feedback > 100):
        print("Invalid Input! Scores must be between 0 and 100.")
    else:

        # Determine Rating
        if project_score > 90 and attendance > 90 and client_feedback > 90:
            rating = "Excellent"

        elif project_score > 75 and attendance > 75 and client_feedback > 75:
            rating = "Good"

        elif project_score > 60 and attendance > 60 and client_feedback > 60:
            rating = "Average"

        else:
            rating = "Poor"

        # Additional Rule
        if attendance < 70 and rating in ["Excellent", "Good"]:
            rating = "Average"
            print("Performance Rating:", rating)
            print("Reason: Attendance below 70%")
        else:
            print("Performance Rating:", rating)

except ValueError:
    print("Invalid Input! Please enter numeric values only.")
    #-------------------------------------------------------------------------
    '''output1:
    Enter Project Score: 95
    Enter Attendance Percentage: 65
    Enter Client Feedback Score: 92
    Performance Rating: Average
    Reason: Attendance below 70%'''

    
    
