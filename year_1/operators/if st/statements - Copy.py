phone_number_db= "0753314934"
email_ad_db= "gundu,boo@gmail.com"
password_db= "gundu123"

user_entry=input("valid email or phone number")
if phone_number_db==user_entry or email_ad_db==user_entry:
#if False:
    #print("proceed")
    password= input("Enter your password")



#Nested if 
if password==password_db:
    print("successfuly logged in")
    #if 
else:
    print("wrong number try again")


        






# conditional operators
# == True or false
# >= True or false
# <= True or false
# /= True or false
# > True or false
# < True or false

# OR operators
# True or True = True
# True or False= True 
# False or False= False

# And operators
# True and True= True 
# True and false= False
# False and false= False