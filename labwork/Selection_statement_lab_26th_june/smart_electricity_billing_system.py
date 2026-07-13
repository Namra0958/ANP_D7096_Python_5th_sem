#Smart Electricity Billing System
'''Problem Statement
Calculate electricity bill using:
Units
Rate
0-100
₹5/unit
101-300
₹7/unit
Above 300
₹10/unit
Additional Rules:
•
Commercial consumers pay 20% extra.
•
Bills above ₹5000 attract 5% surcharge.
•
Senior citizens receive 10% discount.
---------------------------------------------------------------------------------------------------------
Sample Input
Units Consumed: 450 Consumer Type (Residential/Commercial): Commercial Senior Citizen (Y/N): Y
-----------------------------------------------------------------------------------------------------------
Sample Output
Base Bill: ₹4500 Commercial Charge: ₹900 Surcharge: ₹270 Senior Citizen Discount: ₹567 Final Bill Amount: ₹5103
#-------------------------------------------------------------------------------------------------------------'''
#-----------------------------coding------------------------------------------------------------
# WAP for Smart Electricity Billing System with Validation

try:
    units = int(input("Enter Units Consumed: "))
    consumer_type = input("Enter Consumer Type (Residential/Commercial): ").capitalize()
    senior_citizen = input("Senior Citizen (Y/N): ").upper()

    # Validation
    if units < 0:
        print("Invalid Input! Units cannot be negative.")

    elif consumer_type not in ["Residential", "Commercial"]:
        print("Invalid Consumer Type! Enter Residential or Commercial.")

    elif senior_citizen not in ["Y", "N"]:
        print("Invalid Input! Enter Y or N only.")

    else:
        # Calculate Base Bill
        if units <= 100:
            base_bill = units * 5
        elif units <= 300:
            base_bill = units * 7
        else:
            base_bill = units * 10

        print("Base Bill: ₹", base_bill)

        # Commercial Charge
        commercial_charge = 0
        if consumer_type == "Commercial":
            commercial_charge = base_bill * 0.20
            print("Commercial Charge: ₹", commercial_charge)

        total_bill = base_bill + commercial_charge

        # Surcharge
        surcharge = 0
        if total_bill > 5000:
            surcharge = total_bill * 0.05
            print("Surcharge: ₹", surcharge)

        total_bill += surcharge

        # Senior Citizen Discount
        discount = 0
        if senior_citizen == "Y":
            discount = total_bill * 0.10
            print("Senior Citizen Discount: ₹", discount)

        final_bill = total_bill - discount

        print("Final Bill Amount: ₹", final_bill)

except ValueError:
    print("Invalid Input! Please enter numeric values.")
#------------------------------------------------------------------------------------
'''output:
Units Consumed: 450
Consumer Type (Residential/Commercial): Commercial
Senior Citizen (Y/N): Y
Base Bill: ₹ 4500
Commercial Charge: ₹ 900
Surcharge: ₹ 270
Senior Citizen Discount: ₹ 567
Final Bill Amount: ₹ 5103'''