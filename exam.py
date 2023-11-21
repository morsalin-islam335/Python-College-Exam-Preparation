"""
||------------------------------||
||  All Praise to Allah         ||
||------------------------------||
||       Morsalin Islam         ||
||     Department of CST        ||
||SPI, 2nd Shift 2nd Semester   ||
||------------------------------||

"""

############# Determine the area of a right triangle #####################    (সমকোণী ত্রিভুজের খেত্রফল নির্ণয় )

base = int(input("Enter base : "))  # base input নেওয়া
height = int(input("Enter height : "))  # height input নেওয়া
area = 0.5*base* height
print("Area is :", area)



############# Determine the area of the isosceles triangle  #####(বিষম বাহু ত্রিভুজের খেত্রফল নির্ণয় ) ########
import math
arm1 = int(input("Enter arm-1 :"))  # take input
arm2 = int(input("Enter arm-2 :"))   # take input
arm3 = int(input("Enter arm-3 :"))   # take input

if arm1 > arm2 + arm3 or arm2 > arm1+ arm3 or arm3 > arm1 + arm2:
    print("Triangle is not possible")
else:
    s = (arm1 + arm2+ arm3)/2  # অর্ধ - পরিসীমা 
    area = math.sqrt(s* (s-arm1) * (s-arm2) * (s-arm3))  # formula

    print("Area of triangle is :", area)

################# Determine the area of a circle #############

radius = int(input("Enter radius of the circle :")) # take input

pi = 3.1416

area = pi * radius * radius

print("The area of circle is :", area)




################ Program to determine largest number form 3 numbers ####################

num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
num3 = int(input("Enter third number :"))

if num1 > num2 and num1 > num3: ########## first program will be check if if fail than go to elif if its fail than program will be go else statement
    print("largest is", num1)
elif num2 > num1 and num2 > num3:
    print("largest is ", num2)
else:
    print("largest is ", num3)



################# Program to print your name n times ################

name = input("Enter your name")
n = int(input("How many times do you want to repeat your name ? :"))

for i in range(n):
    print(name)



############### 1 + 2 + 3 + 4 + ..................+n = ? #########################

n = int(input("Enter last number :")) # take last number as input (লাস্ট নাম্বার ইনপুট নেওয়া)
sum = 0  # এইটা লুপ এ বার বার যোগ হতে থাকবে।
for i in range(1,n+1,1): # range(start, stop, step)
    sum = sum+i  # এইটা বার বার i এর সাথে যোগ হতে থাকবে।
print("sum is ", sum)



############### 1 * 2 * 3 * 4 * ..................*n = ? #########################

n = int(input("Enter last number :")) # take last number as input (লাস্ট নাম্বার ইনপুট নেওয়া)
sum = 1  # এইটা লুপ এ বার বার গুন হতে থাকবে।
for i in range(1,n+1,1): # range(start, stop, step)
    sum = sum * i  # এইটা বার বার i এর সাথে গুন হতে থাকবে।
print("sum is ", sum)


############### 10 + 20 + 30 + 40 + ..................+n = ? #########################

n = int(input("Enter last number :")) # take last number as input (লাস্ট নাম্বার ইনপুট নেওয়া)
sum = 0  # এইটা লুপ এ বার বার যোগ হতে থাকবে।
for i in range(10,n+1,10): # range(start, stop, step)
    sum = sum+i  # এইটা বার বার i এর সাথে যোগ হতে থাকবে।
print("sum is ", sum)



############## Program to convert temperature from Fahrenheit to Celsius scale ########

f_scale = float(input("Enter temperature of fahrenheit scale :"))
c_scale = ((f_scale - 32) * 9)/5  # Formula
print("Temperature of Celsius Scale is ", c_scale)

################ দ্বি-ঘাত সমীকরণের মুল নির্ণয়ের প্রোগ্রাম ################

# first take input a, b, c

a =  int(input("Enter a :"))
b = int(input("Enter b :"))
c = int(input("Enter c :"))

d = (b*b) - 4*(a*c) # formula  দিয়ে নিশ্চয়ক বের করতে হবে।
if d > 0:  # root will be 2 values
    x1 = (-b + math.sqrt(d))/2*a  # firs semester equation formula
    x2 = (-b - math.sqrt(d))/2*a  # ঐ 
    print("root-1 is :", x1)
    print("root-2 is :", x2)

elif d == 0:  # d = 0 হলে  নিশ্চয়ক হবে ১ টি।
    x = -b / 2*a
    print("root is :", x)

else:
    print("Root will be imaginary")