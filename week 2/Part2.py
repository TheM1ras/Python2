
# 1)print(" *** \n" + "*   *\n"*5+ " *** \n")
# 2)print("**** \n" + "*   *\n"*2 + "**** \n" + "* *\n" + "*  *\n"+ "*   *\n")
"""
#3
age_h = int(input("Input a dogs age in human years: "))
if age_h >=2:
    age_d = 4*(age_h-2) +21
elif age_h ==1:
    age_d = 10.5
else:
    age_d = 0
print("Dogs age in dog years:", age_d)
"""
"""
#4
import re 
letter = input("Enter a letter of the alphabet: ")
if re.search("[aeuio]", letter):
    print(letter, "is a vawel")
else:
    print(letter, "is consonat")
"""
"""
#5
print("list of months: January, February, March, April, May, June, July, August, September, October, November, December")
month = input("Input a month: ")
if month == "February":
    print("number of days: 28/29 ")
elif month == "January" or "March" or "May" or "July" or "August" or "October" or "December":
    print("Number of days: 31")
else:
    print("Number of days: 30")
"""
"""
#6
a = int(input())
b = int(input())
if a + b in range(15, 20):
    print(20)
else:
    print(a+b)
"""
"""
#7
word = input("Input a string: ")
if word.isdigit():
    print("The string is not an integer")
else:
    print("The word is a string")
"""
"""
#8
print("input lenghs of the triangles sides: ")
x = int(input())
y = int(input())
z = int(input())
if x == y == z:
    print("The triangle is equilateral")
elif x== y or y == z or z ==x:
    print("The triangle is isosceles")
else:
    print("The rtiangle is scalene")
"""
"""
#9
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
n = int(input("Enter a month [1-12]: "))
d = int(input("enter a day: "))
print("Date:", months[n-1], d)
if 3<=n<=5:
    print("the seasoon is spring")
elif 6<=n<=8:
    print("the season is summer")
elif 9<=n<=11:
    print("the season is autumn")
else:
    print("the season is winter")
"""
"""
#10
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
d = int(input("Input day of birth: "))
m = input("input month of birth: ")
sign = ""
if m == months[2] and d>= 21 or m == months[3] and d<=19:
    sign = "Aries"
elif m==months[3] and d>=20 or m==months[4] and d<=20:
    sign ="Taurus"
if m == months[4] and d>= 21 or m == months[5] and d<=20:
    sign = "Gemini"
if m == months[5] and d>= 21 or m == months[6] and d<=22:
    sign = "Cancer"
if m == months[6] and d>= 23 or m == months[7] and d<=22:
    sign = "Leo"
if m == months[7] and d>= 23 or m == months[8] and d<=22:
    sign = "Virgo"
if m == months[8] and d>= 23 or m == months[9] and d<=22:
    sign = "Libra"
if m == months[9] and d>= 23 or m == months[10] and d<=21:
    sign = "Scorpio"
if m == months[10] and d>= 22 or m == months[11] and d<=21:
    sign = "Sagittarius"
if m == months[11] and d>= 22 or m == months[0] and d<=19:
    sign = "Capricorn"
if m == months[0] and d>= 20 or m == months[1] and d<=18:
    sign = "Aquarius"
if m == months[1] and d>= 19 or m == months[2] and d<=20:
    sign = "Pisces"
print(sign)
"""
"""
#11
n = int(input("Input year: "))
sign = ""
if n%12 == 0:
    sign = "Monkey"
if n%12 == 1:
    sign = "Rooster"
if n%12 == 2:
    sign = "Dog"
if n%12 == 3:
    sign = "Pig"
if n%12 == 4:
    sign = "Rat"
if n%12 == 5:
    sign = "Ox"
if n%12 == 6:
    sign = "Tiger"
if n%12 == 7:
    sign = "Rabbit"
if n%12 == 8:
    sign = "Dragon"
if n%12 == 9:
    sign = "Snake"
if n%12 == 10:
    sign = "Horse"
if n%12 == 11:
    sign = "Goat"    
print("Your sign:", sign)
"""
"""
#12
y = int(input("input 1st number: "))
m = int(input("Input 2nd number: "))
d = int(input("Input 3rd number: "))
if y<m<d or d<m<y:
    print("median is", m)
if y<d<m or m<d<y:
    print("median is", d)
if m<y<d or d<y<m:
    print("median is", y)
"""
"""
#13
import datetime
y = int(input("input year: "))
m = int(input("Input month: "))
d = int(input("Input day: "))
date = datetime.date(y, m, d)
print(date + datetime.timedelta(days=1))
"""
"""
#14
n = int(input())
sum = 0
for i in range(n+1):
    sum+=i
print(sum, sum/n)
"""
"""
#15
n = int(input("input a number: "))
for i in range(11):
    print(i, "*", n, "=", i*n)
"""
"""
#16
i = 1
for i in range(10):
    for j in range(i):
        print(i, end="")
    print("")
"""
"""
#17
datalist = [1452, 11.23, 1+2j, True, 'student', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]
for item in datalist:
    print(type(item))
"""
for i in range(7):
    if i ==3 or i == 6:
        continue
    else:
        print(i, end=" ")