#signing in first time
print("welcome to gundu hub.chrome")
first_name= input("Enter First name")
last_name= input("Enter last name")
email= input("enter ur email")
password= input("please enter your password")

# now signing in new user 
print("please re-enter your details for verification")
checking_ur_email= input("please re-enter your email")
checking_password= input("please re enter ur password")

#verifying email and password
if checking_ur_email==email:
    print("successfully signed in. Welcome MR.",first_name,last_name, "to the gundu hub,com")
else:
    print("sorry, please enter correct details.")
if checking_password== password:
    print("successfully verified,u may proceed")
else:
    print("invalid access")          
