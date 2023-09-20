nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num_odd = 0
num_even = 0
for item in nums:
    if item % 2==0:
        num_even +=1
    else:
        num_odd +=1
print("Even numbers:", num_even, "\n" + "Odd numbers:", num_odd)