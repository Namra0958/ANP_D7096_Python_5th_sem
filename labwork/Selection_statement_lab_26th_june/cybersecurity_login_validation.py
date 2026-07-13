#Cybersecurity Login Validation
'''Problem Statement
A login system validates:
•
Username
•
Password
•
OTP
Conditions:
•
All correct → Login Successful
•
Incorrect OTP → Re-enter OTP
•
Incorrect Password after 3 attempts → Account Locked
•
Incorrect Username → User Not Found
--------------------------------------------------------------------------
Sample Input
Username: admin Password: admin123 OTP: 4567
---------------------------------------------------------------------------
Sample Output
Login Successful Welcome Admin
#--------------------------------------------------------------------------'''
#------------------------coding----------------------------------------
# WAP for Cybersecurity Login Validation with Validation

correct_username = "admin"
correct_password = "admin123"
correct_otp = "4567"

username = input("Enter Username: ")

# Check Username
if username != correct_username:
    print("User Not Found")

else:
    attempts = 3

    while attempts > 0:
        password = input("Enter Password: ")

        if password == correct_password:
            otp = input("Enter OTP: ")

            if otp == correct_otp:
                print("Login Successful")
                print("Welcome Admin")
            else:
                print("Incorrect OTP")
                print("Re-enter OTP")
            break

        else:
            attempts -= 1

            if attempts == 0:
                print("Account Locked")
            else:
                print("Incorrect Password")
                print("Attempts Left:", attempts)
#--------------------------------------------------------------------
'''output: 
Enter Username: admin
Enter Password: admin123
Enter OTP: 4567
Login Successful
Welcome Admin'''