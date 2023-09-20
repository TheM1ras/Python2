i = int(input())
j = int(input())
lst1 = []
lst2 = []
for a in range(i):
    lst1 = []
    for b in range(j):
        lst1.append(a*b)
    lst2.append(lst1)
print(lst2)