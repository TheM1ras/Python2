list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
x = int(input())
ans = bool(False)
for item in list:
    if x == item:
        ans = True
        break
    else:
        continue
print(ans)
    