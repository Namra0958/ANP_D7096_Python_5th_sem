'''Problem statement
A bank evaluates loan applications using:
•
Credit Score ≥ 750
•
Annual Income ≥ ₹8,00,000
•
Existing Loan Amount ≤ ₹2,00,000
Conditions:
•
All conditions satisfied → Approved
•
Only one condition fails → Manual Review
•
More than one condition fails → Rejected
------------------------------------------------------------------------------------------
Sample Input
Enter Credit Score: 780 Enter Annual Income: 750000 Enter Existing Loan Amount: 100000
-----------------------------------------------------------------------------------------
Sample Output
Loan Status: Manual Review Reason: Income criteria not satisfied.
-------------------------------------------------------------'''
#-----------------------coding ---------------------------
#input from user
# WAP to evaluate a bank loan application with validation

try:
    credit_score = int(input("Enter Credit Score: "))
    annual_income = float(input("Enter Annual Income: "))
    existing_loan = float(input("Enter Existing Loan Amount: "))

    # Validation
    if credit_score < 0 or annual_income < 0 or existing_loan < 0:
        print("Invalid Input! Values cannot be negative.")
    else:
        failed_conditions = []
        
        if credit_score < 750:
            failed_conditions.append("Credit Score criteria not satisfied")
        
        if annual_income < 800000:
            failed_conditions.append("Income criteria not satisfied")
        
        if existing_loan > 200000:
            failed_conditions.append("Existing Loan Amount criteria not satisfied")

        # Loan Decision
        if len(failed_conditions) == 0:
            print("Loan Status: Approved")

        elif len(failed_conditions) == 1:
            print("Loan Status: Manual Review")
            print("Reason:", failed_conditions[0])

        else:
            print("Loan Status: Rejected")
            print("Reasons:")
            for reason in failed_conditions:
                print("-", reason)

except ValueError:
    print("Invalid Input! Please enter numeric values only.")
    #---------------------------------------------------------------------
    '''output1:
    #Enter Credit Score: 780
    # Enter Annual Income: 750000
    # Enter Existing Loan Amount: 100000
    # Loan Status: Manual Review
    # Reason: Income criteria not satisfied.
    #output2:
    # Enter Credit Score: 700
    # Enter Annual Income: 900000
    # Enter Existing Loan Amount: 250000
    # Loan Status: Rejected
    # Reasons:
    # - Credit Score criteria not satisfied'''
    
