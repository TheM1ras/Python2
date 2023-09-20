n = list()
n.append(0)
n.append(1)

m = int(input("How many iterations should the sequence do? "))

print(n[0], n[1], end=" ")

for i in range(m-2):
    n.append(n[len(n)-1]+ n[len(n)-2])
    print(n[len(n)-1], end=" ")