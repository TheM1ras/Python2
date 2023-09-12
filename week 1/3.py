x = str(input())
data =  x.rsplit(" ")
i = 1
while i <= len(data):
    print(data[len(data) - i])
    i+=1