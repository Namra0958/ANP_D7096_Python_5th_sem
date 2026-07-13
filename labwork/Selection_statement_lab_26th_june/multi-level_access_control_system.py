#Multi-Level Access Control System
'''Problem Statement
Assign access levels based on:
Roles:
•
Admin
•
Manager
•
Employee
•
Guest
Conditions:
•
Admin + Security Clearance ≥ 5 → Full Access
•
Manager + Experience > 5 Years → Department Access
•
Employee + Experience > 2 Years → Limited Access
•
Guest → Read-Only Access
•
Inactive Account → No Access
-------------------------------------------------------------------------
Sample Input
Role: Admin Security Clearance: 6 Account Status: Active
------------------------------------------------------------------------
Sample Output
Access Level: FULL ACCESS
#--------------------------------------------------------------------------'''
#--------------------------------coding----------------------------------
# WAP for Multi-Level Access Control System with Validation

role = input("Enter Role (Admin/Manager/Employee/Guest): ").capitalize()

if role not in ["Admin", "Manager", "Employee", "Guest"]:
    print("Invalid Role!")

else:
    account_status = input("Enter Account Status (Active/Inactive): ").capitalize()

    if account_status not in ["Active", "Inactive"]:
        print("Invalid Account Status!")

    elif account_status == "Inactive":
        print("Access Level: NO ACCESS")

    else:
        if role == "Admin":
            security_clearance = int(input("Enter Security Clearance: "))

            if security_clearance >= 5:
                print("Access Level: FULL ACCESS")
            else:
                print("Access Level: NO ACCESS")

        elif role == "Manager":
            experience = float(input("Enter Experience (Years): "))

            if experience > 5:
                print("Access Level: DEPARTMENT ACCESS")
            else:
                print("Access Level: NO ACCESS")

        elif role == "Employee":
            experience = float(input("Enter Experience (Years): "))

            if experience > 2:
                print("Access Level: LIMITED ACCESS")
            else:
                print("Access Level: NO ACCESS")

        elif role == "Guest":
            print("Access Level: READ-ONLY ACCESS")
#---------------------------------------------------------------------------
'''output: 
Role: Admin
Security Clearance: 6
Account Status: Active
Access Level: FULL ACCESS'''