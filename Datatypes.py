# Datatypes in Python
# 1.int → numbers (10, -5, 100)
# A.Add of two number
'''a=10
b=30
sum=a+b
print("Sum of number:-",sum)'''

# B.Subtract of two number.
'''a=10
b=5
c=3
sub=a-b-c
print("Subtract of Number:-",sub)'''

# ^INPUTING METHOD:-
# A.Add of Number
'''a=int(input("enter the 1st value :-"))
b=int(input("Enter the 2nd value:-"))
sum=a+b
print("Sum of Numbers:-",sum)'''

# 2.float → decimal numbers (3.14, -2.5)
# A.Sum of Decimal number
'''a=45.4
b=77.1
sum =a+b
print("sum of numbers:-",sum)'''
# B.Subtract of Decimal number
'''a=99.3
b=96.44
sub=a-b
print("Subtract of Number:-",sub)'''

# ^ Inputing Method
# Add of Two number 
'''a=float(input("Enter the 1st Number:-"))
b=float(input("enter the 2nd number:-"))
sum=a+b
print("The sum of number:-",sum)'''
# Subtract of two number
'''a=float(input("Enter the 1st Number:-"))
b=float(input("enter the 2nd number:-"))
sum=a-b
print("The sum of number:-",sum)'''

# 3.str → text/strings ("Hello", 'Python')
'''str="Python Programing"
print(str[0])
print(str[0:18])
print(len(str))'''
# Common String Method:-
'''str="Python Programing"
print(str.upper())
print(str.lower())
print(str.capitalize())
print(str.strip())
print(str.replace("Programing","Hello"))'''

#Q1.Take user input and print length
'''word=input("Enter a word:-")
print("Length is :-",len(word))'''
#Q2.Check if "python" exists in string
'''sentance=input("Enter a sentance:-")
print("Python"in sentance )'''

# 4.bool → True / False
'''word="Wel come to  python programing"
print("python"in word)  # it is a present in row.
print("well"in word) # it is not present in row.'''

# 5.list → [1, 2, 3] it is mutable(changeable)
'''list=[1,2,3]
print(list[0])
print(list[1])
print(list[2])'''

# Q1. 
'''fruits=["Apple","Banana","Mango"]
print(fruits[0])
fruits.append("cherry")
print(fruits)
fruits[0]="Grapes"
print(fruits)'''
# 6.tuple → (1, 2, 3) it is a immutable
'''data=(1,2,3)
print(data[0])'''

#Q1.Store marks of 5 students
'''marks=(50,60,89,74,64)
print("average",sum(marks)/len(marks))'''

# Q2: Tuple test
'''t=(2,56,3,2,67,4,56)

print(t.count(2))
print(t.index(56))'''

# 7.set → {1, 2, 3}
'''num={1,2,2,3,4}
print(num)
num.add(5)
print(num)'''

# Q2: Unique numbers using set
'''nums=[1,2,2,3,4,2,2,5]
unique=set(nums)
print(unique)'''
# 8.dict → {"key": "value"}
'''student={
    "Name":"Sudhir Kumar Singh",
    "age":23,
    "Course":"Python"
}
print(student["Name"])
student["age"]=24
print(student.get("marks","Not Found"))'''

# Q1: Create dictionary
'''info={
    "Name":"Sudhir",
    "Language": ["Python","SQL","C++"]
}
info["Language"].append("Java")
print(info["Language"])'''
# 9.None → null (empty)c

#^Numbers (int, float, bool):-
#Q1.Take two integer inputs from the user and print their sum, difference, product, and division.
'''a=int(input("Enter the 1st value:-"))
b=int(input("Enter the 2nd value:-"))
add=a+b
sub=a-b
mul=a*b
div=a/b
print("addtion=",add,"\n","subtract=",sub,"\n","Multiplay=",mul,"\n","divide=",div)'''

#Q2.Take a float number as input and print its square and cube.
'''import math
radius=float(input("enter the value radius of circle:-"))
circle_area=math.pi * radius **2
print("Area of Circle:-",circle_area)
side=float(input("enter the value side of squre "))
square_area=side **2
print("Area of squre:",square_area)'''

#Q3.Check whether a given number is even or odd (also check its datatype).
'''num=int(input("enter the number :-"))
print(type(num))
if num%2==0:
    print("number is odd")
else:
    print("num is even")'''
    
#Q4.Create a boolean variable and check its datatype using type().
'''is_devloper=True
is_student=False

print("Datatypes of is_devloper",type(is_devloper))
print("Datatype of Is_student",type(is_student))'''

#Q5.Take two numbers as input and find the greater and smaller number using max() and min().
'''a=int(input("enter the 1st value :-"))
b=int(input("enter the 2nd value :-"))
greater=max(a,b)
smallest=min(a,b)
print("greater number is:-",greater)
print("Smaller number is :-",smallest)'''

#* Method2
'''num=[34,76,43,90,434]
greater=max(num)
smallest=min(num)

print("greater is ",greater)
print("smallest is ",smallest)'''

#^ String (str)
#Q6.ake the user’s name and print it in uppercase, lowercase, and also print its length.



