#Q1.Find you are eligable for voting.
'''age=int(input("Enter your age:-"))
if(age>=18):
    print("You are eligible for votting")
else:
    print("You are not eligible for voting")'''
    
#Q2.Find a grade of Student
'''marks=float(input("enter a marks as you find a grade of Students:-"))
if marks >=90:
    print("Grade A")
elif marks >=79:
    print("Grade B")
elif marks >=69:
    print("Grade C")
else:
    print("Fail")'''
    
#Q3. Student Result deatils:-
'''name=input("enter your name :-")
password=input("Enter password to access student see Result:-")
if password != "1234":
    print("Access Denied ")
    exit()
print("Access Granted \n")

hindi=float(input("Enter the Hindi marks:-"))
english=float(input("Enter the English Marks:- "))
math=float(input("Enter the math marks:-"))
Science=float(input("Enter the Science Marks:-"))
computer=float(input("Enter the Computer marks :-"))
total=hindi+english+math+Science+computer
subjects=5
percentage=(total/(subjects*100))*100
print("Total marks :-",total)
print("Percentage :-",percentage,"%")
# Division
if percentage>=60:
    print("First Division")
elif percentage >= 49:
    print("Second Division")
elif percentage >=39:
    print("Third Division")
else:
    print("fail")
    
# Grade 
if percentage >=60:
    print(" Grade :- A++")
elif percentage >=49:
    print(" Grade B")
elif percentage >=39:
    print(" Grade C")
else:
    print(" Fail")'''
    
#Q4.Even or Odd
'''user=float(input("Enter the number :-"))
if user % 2==0:
    print("Num is odd")
else:
    print("Num id odd")'''
    
#Q5.Greatest of Two Numbers
'''a=float(input("Enter the 1st number:-"))
b=float(input("Enter the 2nd number :-"))

if a>b:
    print(a,"is grater")
elif b>a:
    print(b,"b is grater")
else:
    print("Both are equal")'''
    
#Q6.Leap Year Check.
'''year=int(input("Enter the year :-"))
if year % 4==0:
    print("leap Year")
else:
    print("not leap year")'''

#Q7.Positive, Negative or Zero.
'''num=float(input("enter the number:-"))
if num > 0:
    print("Positive number")
elif num <0:
    print("Negative Number")
else:
    print("Zero number")'''
    
# Q8.Divisible Check
'''num=float(input("enter the value:-"))
if (num % 5 == 0) and (num % 11 == 0):
    print("it is divisible by 5 and 11")
else:
    print("it is not divisible by both")'''

#Q9.Calculator
'''a=float(input("enter the 1st value :-"))
b=float(input("enter the 2nd value:-"))

add=a+b
print("addition is :-",add)

sub=a-b
print("Subtract is :-",sub)

mul=a*b
print("Multiply is :-",mul)

div=a/b
print("divide is :-",div)'''
    
    