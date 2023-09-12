import math
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
xc = (x1+x2+x3)/3
yc = (y1+y2+y3)/3
print("Central coordinates: ", xc, yc)
print("radius of a circle: ",math.sqrt((x3- xc)**2 + (y3 - yc)**2))