# Write a Python program to check the validity of password input by users.
# Validation :
# 1. At least 1 letter between [a-z] and 1 letter between [A-Z]
# 2. At least 1 number between [0-9]
# 3. At least 1 character from [$#@]
# 4. minimum length 6 characters
# 5. maximum length 16 characters
# 6. Can't contain spaces.

import re
p= raw_input("Input your password:")
x = True
while x:
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break
if x:
    print("Not a Valid Password")