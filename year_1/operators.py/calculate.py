# pick the first number from the user

print("welcome to the simple calculator")
print

print("please enter the first number")
first_number=int(input())

print("hurrrrreyyyy")
print("now, select 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division")
print("1,+")
print("2,-")
print("3,*")
print("4,/")

operator=int(input())
print("wooop woooop")
print("please enter the second number")
second_number=int(input())

right_answer=0
if operator== 4:
    print("what is",first_number,"/",second_number)
    right_answer= first_number/second_number

ans=int(input())


if right_answer==ans:
    print("correct")
else:
    print("wrong answer")   















