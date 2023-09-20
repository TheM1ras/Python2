op = int(input("C-F 1: \nF-C 2: \n"))
if op == 1:
    t = int(input())
    print( t, "C=", t*1.8 + 32, "F")
if op == 2:
    t = int(input())
    print(t, "F=", (t-32)/1.8, "C")