'''Airline Ticket Pricing Engine
Problem Statement
An airline calculates ticket fare using:
Base Fare = ₹5000
Additional Charges:
•
Business Class → +₹3000
•
Window Seat → +₹500
•
Weekend Travel → +₹1000
Discounts:
•
Age below 12 → 50%
•
Age above 60 → 20%
Calculate the final ticket fare.
----------------------------------------------------------------------------------------------
Sample Input
Enter Passenger Age: 65 Business Class (Y/N): Y Window Seat (Y/N): Y Weekend Travel (Y/N): Y
-------------------------------------------------------------------------------------------------
Sample Output
Base Fare: ₹5000 Additional Charges: ₹4500 Senior Citizen Discount: 20% Final Ticket Fare: ₹7600.0
----------------------------------------------------------------------------------------------------------'''
#---------------------------------------coding-----------------------------
# WAP to calculate Airline Ticket Fare with Validation

try:
    age = int(input("Enter Passenger Age: "))

    if age < 0:
        print("Invalid Age! Age cannot be negative.")
    else:
        business = input("Business Class (Y/N): ").upper()
        window = input("Window Seat (Y/N): ").upper()
        weekend = input("Weekend Travel (Y/N): ").upper()

        # Validation
        if business not in ['Y', 'N'] or window not in ['Y', 'N'] or weekend not in ['Y', 'N']:
            print("Invalid Input! Please enter Y or N only.")
        else:
            base_fare = 5000
            additional_charges = 0

            if business == 'Y':
                additional_charges += 3000

            if window == 'Y':
                additional_charges += 500

            if weekend == 'Y':
                additional_charges += 1000

            total_fare = base_fare + additional_charges

            # Apply Discount
            if age < 12:
                discount = 50
                final_fare = total_fare * 0.50
                print("Child Discount: 50%")

            elif age > 60:
                discount = 20
                final_fare = total_fare * 0.80
                print("Senior Citizen Discount: 20%")

            else:
                discount = 0
                final_fare = total_fare

            print("Base Fare: ₹", base_fare)
            print("Additional Charges: ₹", additional_charges)
            print("Final Ticket Fare: ₹", final_fare)

except ValueError:
    print("Invalid Input! Please enter numeric age.")
    #------------------------------------------------------------
    '''output1:
    Enter Passenger Age: 65
    Business Class (Y/N): Y
    Window Seat (Y/N): Y
    Weekend Travel (Y/N): Y
    Base Fare: ₹5000
    Additional Charges: ₹4500
    Senior Citizen Discount: 20%
    Final Ticket Fare: ₹7600.0'''
    