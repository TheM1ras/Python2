import math
n = int(input())
if abs(1000 - n) <= 100 or abs(2000 - n) <= 100:
    print("Yes")
else:
    print("No")