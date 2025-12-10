# Task: Sum All Numbers in a List
# input=[10, 20, 30, 40, 50]
# Expected output : Sum of numbers: 150

l1 = [10, 20, 30, 40, 50]
print("\nInput:", l1)
print("Sum of numbers:", sum(l1))


# Write a Python program that accepts a string and 
# counts the number of upper and lower case letters. 
# Sample String : 'My Name is Sujan' 
# Expected Output : 
# No. of Upper case characters : 3 
# No. of Lower case Characters : 10

str1 = 'My Name is Sujan'
print("\nSample String:", str1)
str2 = input("Enter any String: ")
upper = 0
lower = 0
for i in str2:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
print("No. of Upper case characters :", upper)
print("No. of Lower case Characters :", lower)


# Write a Python program that takes a string and 
# returns a dictionary where:

# Keys are the unique characters in the string
# Values are the counts of each character

# input="aabbssssdka"
# expected Output
# {"a": 3, "b": 2, "s": 4, "d": 1, "k": 1}

str1 = "aabbssssdka"
print("\nSample Input:", str1)
str2 = input("Enter any Input: ")
dict1 = {}
for i in str2:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
print("Output:", dict1)


# Write a Python program to generate and 
# print the first n numbers in the Fibonacci sequence, 
# where each number is the sum of the two preceding ones, 
# starting from 0 and 1.

# 0,1,0+1=1,1+1=2,2+1=3,3+2=5,5+3=8,8+5=13

a = 0
b = 1
print("\nFibonacci sequence")
num = int(input("Enter nth term: "))

for i in range(num):
    print(a, end=" ")
    temp = a+b
    a = b
    b = temp


# Task:
# Python program to check the validity of password input by users
# At least 8 characters long.
# Contains at least one uppercase letter.
# Contains at least one lowercase letter.
# Contains at least one digit.
# Contains at least one special character
# note: Clearly indicate which specific requirements were not met

password = input("\n\nPassword: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

special_characters = "!@#$%^&*()-_+=[]{}|;:'\",.<>/?`~"

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    elif ch in special_characters:
        has_special = True

errors = []

if len(password) < 8:
    errors.append("Password must be at least 8 characters long.")
if not has_upper:
    errors.append("Password must contain at least one uppercase letter.")
if not has_lower:
    errors.append("Password must contain at least one lowercase letter.")
if not has_digit:
    errors.append("Password must contain at least one digit.")
if not has_special:
    errors.append("Password must contain at least one special character (!@#$%^&*).")
if " " in password:
    errors.append("Password must not contain any spaces.")

if len(errors) == 0:
    print("Valid Password")
else:
    print("Invalid Password:")
    for error in errors:
        print("-", error)