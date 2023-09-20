import re
test = input()

a= re.findall("[a-zA-Z]", test)
b = re.findall("[0-9]", test)
print("letters:",len(a) )
print("numbers:", len(b))