
##
##name="sanjay"  #global scope
##def my_function():
##    name="san"  #local scope
##    print(name,"inside the function")
##my_function()
##print(name,"outside the function")
##
###
##def ocean(software):
##    print(software,"before return")
##    return software
##    print(software,"after return")
##print(ocean("academy"))
##
###
##team="mumbai indians"   #global scope
##def my_function():
##    colour="blue"                     #local scope
##    print(colour,"inside the function")
##my_function()
##print(team,"outside the function")

##8#leap year
##def leap_year(year):
##    if(year%4==0):
##        print(year,"is a leap year")
##    else:
##        print(year,"is not a leap year")
##leap_year(int(input("Enter the year:")))
##
##
##10#Largest Number
##a=int(input("Enter a:"))
##b=int(input("Enter b:"))
##def largest_number(a,b):
##    if(a>b):
##        print(a,"is largest number")
##    elif(a<b):
##        print(b,"is largest number")
##    elif(a==b):
##        print(a,"and",b,"are equal")
##largest_number(a,b)
##
####checking three pesons salary
##a=int(input("ENTER SALARY OF PERSON A:"))
##b=int(input("ENTER SALARY OF PERSON B:"))
##c=int(input("ENTER SALARY OF PERSON C:"))
##
##def my_function(a):
##    print(a)
##if(c<b and c<a):
##    print("C IS MINIMUM")
##elif(a<b and a<c):
##    print("A IS MINIMUM")
##elif(b<c and b<a):
##    print("B IS MINIMUM")
##else:
##    ("three salaries are equal ")
##my_function(a)
##
##
###odd or even 
##a=int(input("Enter a number:"))
##def function(a):
##    if a%2==0:
##        print("The number is even")
##    else:
##        print("The number is odd")
##function(a)
##
###
##a = int(input("Enter a percentage: "))
##b = int(input("Enter b percentage: "))
##
##def my_function(a, b):
##    print(f"Percentage A: {a}")
##    if a >= 90:
##        print("Grade: S")
##    elif a >= 80:
##        print("Grade: G")
##    elif a >= 70:
##        print("Grade: F")
##    elif a >= 30:
##        print("Grade: E")
##    elif a >= 15:
##        print("Grade: D")
##    elif a >= 10:
##        print("Grade: C")
##    elif a >= 5:
##        print("Grade: B")
##    else:
##        print("Grade: A")
##
##my_function(a, b)
##
###
##def classify_triangle(a):
##    if a == 3:
##        print("This is an Equilateral Triangle")
##    elif a == 2:
##        print("This is an Isosceles Triangle")
##    elif a == 1:
##        print("This is a Scalene Triangle")
##    else:
##        print("not valid : A triangle must have at least one side equal to another.")
##
###MONTHS AND SEASONS
##months=input("enter month to find season:")
## def my_function(a):
##    print(a)
##if months in("june","july","augest","september"):
##    print("Moonsoon Season")
##elif months in("october","september","november"):
##    print("Autumn Season")
##elif months in("december"):
##    print("Pre-winter")
##elif months in ("january","february"):
##    print("Winter season")
##elif months in("march","april","may"):
##    print("Summer season")
##else:
##    print("not a valid season")
##my_funtion (a)
##
##9#2-digit
##def two_digit(num):
##    if(9<num<100):
##        print("It is a two digit number")
##    else:
##        print("It is not a two digit number")
##two_digit(int(input("Enter the num:"))) 

#find second largest number
a=int(input("200"))
b=int(input("120"))
c=int(input("100"))

def second largest(a,b,c):
    if(a>b and a<c) or (a>c and a<b):
        print(a)
    elif(b>a and b<c) or (b>c and b<a):
        print(b)
    else:
        print(c)














