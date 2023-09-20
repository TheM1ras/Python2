for i in range(51):
    if i%3==0 and i%5!=0:
        print("Mkm", end=" ")
    elif i%5==0 and i%3!=0:
        print("KBTU", end=" ")
    elif i%15==0:
        print("MkmKBTU", end=" ")
    else:
        print(i, end=" ")