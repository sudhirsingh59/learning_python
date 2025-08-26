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

'''name=input("Enter your name:-")
print("Uppercase:",name.upper())
print("Lowercase:",name.lower())
print("Length:",len(name))'''

#Q7.Take a sentence as input and count how many words it has.
'''sentence=input("Enter a sentence:-")
words=sentence.split()
print("Total words in the sentacne:-",len(words))'''

#Q8.Check whether the word "python" exists inside a given string.
'''text=input("enter the text:-")
if "python" in text:
    print("it is exists in string")
else:
    print("it is not exists in string")'''
    
#Q9.Take a string from the user and print it in reverse.
'''text=input("enter the text:-")
reverse=text[::-1]
print("The reverse text is :-",reverse)'''

#Q10.Print the first and last character of a given string.
'''text=input("enter the text :-")
if len (text) > 0:
    print("first character:-",text[0])
    print("Last character :-",text[-1])
else:
    print("String is empty !")'''
    
#^List
#Q1.reate a list of 5 numbers and calculate the sum and average.
'''list=[34,56,98,32,12]
total=sum(list)
average=total/len(list)
print("List of numbers:",list)
print("sum",total)
print("Average",average)'''
#Q2.Add, remove, and update an element in a list.
'''data=["mango","apple","banana"]
print("Orignal List",data)
data.append("garpes")
print("After add garpes",data)
data.remove("mango")
print("After removing mango",data)
data[1]="orange"
print("After uodating banana: ",data)'''

#Q3.Sort a list in ascending order and print it.
'''list=[98,43,90,43,34,1]
print("Orignal list:-",list)
list.sort()
print("Sortes list :-",list)'''

#Q.Sort a list in ascending order and print it.
'''list=[98,43,90,43,34,1]
print("Orignal List:-",list)
list.sort(reverse=True)
print("Sorted list(Descending):",list)'''

#Q4.Check whether a particular number exists in a list or not.
'''list=[10,20,30,40,50]
num=int(input("enter the value :-"))
if num in list:
    print(f"{num} exists in the list")
else:
    print("f{num} it is not exist in the loop")'''
    
#Q5.Remove duplicate elements from a list and print the unique list.
'''num=[10,20,30,40,50,10,50,40]
unique_list=list(set(num))
print("unique list :-",unique_list)'''

#^ Tuple
#Q1.Create a tuple and count how many times a particular element appears in it.
'''numbers=(1,3,6,1,5,6)
num=int(input("enter the number to count :-"))
count=numbers.count(num)
print(f"{num} appears {count} times in the tuple")'''

#Q2.Find the index of an element in a tuple.
numbers=(10,20,30,40,50,60,70,80,90,100)
num=int(input("enter the number to find its index:-"))
if num in numbers:
    index=numbers.index(num)
    print(f"The first occurrance of {num} is at index {index}.")
else:
    print(f"{num} is not present in the tuple.")
