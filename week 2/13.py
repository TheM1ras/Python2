import re
password = input()
if re.search("[a-z]", password) and re.search("[A-Z]", password) and re.search('[0-9]', password) and re.search("[@#$]", password) and 6<=len(password)<=12:
    print("Valid password")
else:
    print("password is invalid")