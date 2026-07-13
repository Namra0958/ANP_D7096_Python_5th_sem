#E-Commerce Premium Membership Eligibility
'''Problem Statement
A customer becomes Premium Member if:
•
Total Purchases > ₹50,000
•
Orders Completed ≥ 20
•
Customer Rating ≥ 4.5
Special Case:
•
Purchases above ₹1,00,000 automatically qualify.
---------------------------------------------------------------------------------------
Sample Input
Total Purchases: 120000 Orders Completed: 10 Customer Rating: 4.0
----------------------------------------------------------------------------------------
Sample Output
Premium Membership Status: Eligible Reason: Purchase amount exceeded ₹100000.
#---------------------------------------------------------------------------------'''
#------------------------------------coding------------------------------
# WAP to check E-Commerce Premium Membership Eligibility with Validation

try:
    purchases = float(input("Enter Total Purchases: "))
    orders = int(input("Enter Orders Completed: "))
    rating = float(input("Enter Customer Rating: "))

    # Validation
    if purchases < 0 or orders < 0 or rating < 0 or rating > 5:
        print("Invalid Input! Please enter valid values.")
    else:

        # Special Case
        if purchases > 100000:
            print("Premium Membership Status: Eligible")
            print("Reason: Purchase amount exceeded ₹100000.")

        # Normal Eligibility Check
        elif purchases > 50000 and orders >= 20 and rating >= 4.5:
            print("Premium Membership Status: Eligible")

        else:
            print("Premium Membership Status: Not Eligible")

except ValueError:
    print("Invalid Input! Please enter numeric values only.")
    #------------------------------------------------------------------------
    '''output:
    Enter Total Purchases: 120000
    Enter Orders Completed: 10
    Enter Customer Rating: 4.0
    Premium Membership Status: Eligible
    Reason: Purchase amount exceeded ₹100000.'''