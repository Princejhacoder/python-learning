print("Hello, World!")
print("Prince Jha is my name.")
print(26+26)

# Variables
name = "Prince Jha" #string variable
age = 20 #integer variable
price = 100.50 #float variable

print(name)
print(age)
print(price)

# type of variable
print(type(name))
print(type(age))
print(type(price))

# Data types
age = 23
old = False
a = None
print(type(old))
print(type(a))

# Keywords
# and        else       in        return
# as         except     is        True
# assert     finally    lambda    try
# break      False      nonlocal  with
# class      for        None      while
# continue   from       not       yield
# def        global     or
# del        if         pass
# elif       import     raise


# Print Sum
a = 10
b = 16
sum = a + b
print(sum)

# Type of Operators 

# arithmetic operator
a = 5
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b) # remainder
print(a ** b) #a^b

# Relational / comparison Operator

a = 50 
b = 20

print(a == b) # False
print(a != b) # True
print(a >= b) # True
print(a > b) # True

# Assignment Operator

num = 10
num = num + 10 #10+10 =>20
num +=10
print("num = ", num)

# Logical Operator
# 1. not Operators
a = 50
b = 30
print(not False) # True
print(not (a>b)) # False

# 2.And / Or Operator

val1 = True
val2 = False
print("And operator = ", val1 and val2) # False

print("Or operator = ",(a==b) or (a>b))


# Type Conversion
a = 2
b = 4.25

sum = a + b# 6.25
print(sum)

# Type casting
a = 3.14
a = str(a)

print(type(a))

# input in users

name = input("enter your name : ")
print("Welcome" , name)

val = input("enter some value: ")
print(type(val) , val) #"25" , "99.99"


val = int(input("enter some value: "))
print(type(val) , val)


name = input("enter name :")
age = input("enter age :")
marks = input("enter marks :")

print("Welcome" ,name)
print("age =", age)
print("marks =" , marks)


# Practice Questions

# 1. Write a program to input 2 number and print their sum.

a = int(input("Enter first number :"))

b = int(input("Enter second number :"))

sum = a + b
print("Sum of two number is : ", sum)

# 2. write a program to input side of a square and print its area.

side = int(input("Enter side of square :"))
Area = side * side

print("Area of square is :" , Area)

#3. Write a program to input 2 floating point number and print their average.

a = float(input("Enter first number :"))
b = float(input("Enter second number :"))

average = (a + b) / 2
print("Average of two number is : ", average)

# 4. WAP to input 2 int number , a and b print True if a is greater than or equal to b. if not print False.
a = int(input("Enter first number :"))
b = int(input("Enter second number :"))
print(a >= b) 