from msilib.schema import AdminExecuteSequence
from time import sleep

user = input("Please create a username :")
password = input("Please insert a secure password: ") 


if not any(x.isupper() for x in password):
   print("Password must have one uppercase letter. Please Reload and try again.")
   sleep(3)
   exit
else:
    print("User Created. Please Continue to log in: ")

LoginUser = input("please enter your username: ")

if LoginUser != user:
    print("Incorrect. Exiting in three seconds")
    sleep(3)
    exit
else:
    TempPass = input("Please enter your password: ")
    
if TempPass != password:
    print("Incorrect. Exiting in three")
    sleep(3)
    exit
else: print ("Successfully logged in")