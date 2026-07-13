#University Scholarship System
'''Problem Statement
Scholarship is awarded based on percentage:
Percentage
Scholarship
95+
100%
90-94
75%
85-89
50%
80-84
25%
Below 80
No Scholarship
Conditions:
•
Family income must be below ₹8,00,000.
•
Students with disciplinary actions receive no scholarship.
---------------------------------------------------------------------------------------
Sample Input
Percentage: 92 Family Income: 500000 Disciplinary Action (Y/N): N
---------------------------------------------------------------------------------------
Sample Output
Scholarship Awarded: 75%
#-----------------------------------------------------------------------------------'''
#------------------------------------------coding----------------------------------
# WAP to determine University Scholarship Eligibility with Validation

try:
    percentage = float(input("Enter Percentage: "))
    family_income = float(input("Enter Family Income: "))
    disciplinary_action = input("Disciplinary Action (Y/N): ").upper()

    # Validation
    if percentage < 0 or percentage > 100:
        print("Invalid Percentage! Enter a value between 0 and 100.")

    elif family_income < 0:
        print("Invalid Family Income!")

    elif disciplinary_action not in ['Y', 'N']:
        print("Invalid Input! Enter Y or N only.")

    else:
        # Check eligibility conditions
        if family_income >= 800000:
            print("Scholarship Awarded: No Scholarship")
            print("Reason: Family income exceeds ₹8,00,000.")

        elif disciplinary_action == 'Y':
            print("Scholarship Awarded: No Scholarship")
            print("Reason: Disciplinary action record found.")

        else:
            # Scholarship based on percentage
            if percentage >= 95:
                scholarship = "100%"
            elif percentage >= 90:
                scholarship = "75%"
            elif percentage >= 85:
                scholarship = "50%"
            elif percentage >= 80:
                scholarship = "25%"
            else:
                scholarship = "No Scholarship"

            print("Scholarship Awarded:", scholarship)

except ValueError:
    print("Invalid Input! Please enter numeric values.")
    #-----------------------------------------------------------------
    '''output:
    Enter Percentage: 92
    Enter Family Income: 500000
    Disciplinary Action (Y/N): N
    Scholarship Awarded: 75%'''