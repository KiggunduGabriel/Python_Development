#obtaining stdents marks 
CW_MARKS= 17.5
EX_MARKS=17.5

# obtain the CW_SCORE
cw_score= float(input("Enter your cw score(out of 50):"))
Attendence=input("Did you attend classes? (yes/No): ").lower





# obtaining if the student passed CW and attended classes 
if cw_score >= CW_MARKS and Attendence =="yes":
    print("you passed cw and attendence class.you are allowed to do the exam")
    Ex_score = float(input("Enter your ex score(out of 50): "))
    if Ex_score>= EX_MARKS:
        print("congragulations, you have passed bothe CW and EX,your allowed to go year 1 semster 2")
    else:
        print("sorry you failed. you need to atleast 17.5 of the mark to pass")
    
if cw_score < CW_MARKS:
    print("sorry, you have failed the CW")
else:
    print("SORRY, you had a bad attendence thus you failed")
              











