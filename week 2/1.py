import math
for i in range(1500, 2701):
    if math.fmod(i, 35) == 0:
        print(i)