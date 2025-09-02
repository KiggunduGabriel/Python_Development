# check if a person is eligible to vote
age=int(input("enetr your age"))
#input the country 
nationality= input("enter your country")
nationality_pass= "ugandan"
if nationality==nationality_pass:
    print("you are ugandan")
else:
    print("you are not ugandan,you cant procceed") 
    ages=int(input("how old are you?"))
    age=18
    if age<=ages:
        print("you are eligible")
    else:
        print("you are not eligible ")    


