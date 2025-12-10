#Q.no.1

num = int(input("\nEnter any number: "))
if num % 2 == 0:
    print(num, "is Even Number.")
else:
    print(num, "is Odd Number.")


#Q.no.2

age = int(input("\nEnter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


#Q.no.3

age = int(input("\nEnter age: "))
if age > 0 and age < 100:
    print(age, "is a Valid age.")
else:
    print(age, "is not Valid age.")


#Q.no.4

vowel = ('a', 'e', 'i', 'o', 'u')
letter = input("\nEnter any letter: ")
if letter.lower() in vowel:
    print(letter, "is a Vowel Letter.")
else:
    print(letter, "is a Consonant Letter.")


#Q.no.5

num1 = int(input("\nEnter any Number: "))
if num1 % 5 == 0:
    print(num1, "is divisible by 5")
else:
    print(num1, "is not divisible by 5")


#Q.no.6

marks = int(input("\nStudent's Marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")


#Q.no.7

num = int(input("\nEnter any number: "))
if num >=10 and num <=50:
    print(num, "lies between 10 and 50.")
else:
    print(num, "doesn't lie between 10 and 50.")


#Q.no.8

word = input("\nEnter any Word: ")
reverse_word = word[::-1]
print(reverse_word)
if word.lower() == reverse_word.lower():
    print(word, "is a palindrome.") 
else:
    print(word, "is not a palindrome.") 


#Q.no.9

email = input("\nEmail: ")
if email.endswith('@gmail.com'):
    print(email, "ends with '@gmail.com'")
else:
    print(email, "doesn't end with '@gmail.com'")


#Q.no.10

num1 = int(input("\nFirst Number: "))
num2 = int(input("Second Number: "))

if num1 > num2:
    print(num1, "is greater.")
elif num2 > num1:
    print(num2, "is greater.")
else:
    print("Both are equal")


#Q.no.11

num = int(input("\nEnter any number: "))
if num > 0:
    print(num, "is positive number.")
elif num < 0:
    print(num, "is negative number.")
else:
    print("The given number is zero.")


#Q.no.12

total_bill = int(input("\nTotal Bill: "))

if total_bill > 1000:
  final_bill = total_bill - (total_bill * 0.1)
else:
  final_bill = total_bill
print("Final Bill:", final_bill)


#Q.no.13

num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter Second number: "))
operator = input("Enter an operator(+,-,*,/): ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2 
else:
    result = "Invalid" 
print(result)


#Q.no.14

marks = int(input("\nEnter Student Marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Fail")


#Q.no.15

num1 = int(input("\nEnter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if (num1 >= num2) and (num1 >= num3):
    print(num1, "is the greatest number.")
elif (num2 >= num1) and (num2 >= num3):
    print(num2, "is the greatest number.")
else:
    print(num3, "is the greatest number.")


#Q.no.16

import getpass

username = "admin"
password = "1234"

user_input = input("\nUsername: ")
pass_input = getpass.getpass("Password: ")

if user_input == username and pass_input == password:
    print("Login Successful")
else:
    print("Invalid Credentials")


#Q.no.17

side1 = int(input("\nEnter First Side: "))
side2 = int(input("Enter Second Side: "))
side3 = int(input("Enter Third Side: "))

if (side1 + side2 > side3):
    print("The sides can form a triangle.")
elif (side2 + side3 > side1):
    print("The sides can form a triangle.")
elif (side3 + side1 > side2):
    print("The sides can form a triangle.")
else:
    print("The sides can not form a triangle.")


#Q.no.18

unit = int(input("\nUnit: "))

if unit <= 100:
    bill = unit * 5
elif 100 < unit <= 200:
    bill = unit * 7
elif unit > 100:
    bill = unit * 10
print("Bill:", bill)


#Q.no.19

marks = float(input("\nStudent's marks: "))
attendance = float(input("Student's attendance: "))

if marks > 85 and attendance > 75:
    print("Scholarship is granted.")
else:
    print("Scholarship is not granted.")


#Q.no.20

temperature = float(input("\nTemperature (Celcius): "))

if temperature > 30:
    print("Hot")
elif 15 <= temperature <= 30:
    print("Warm")
else:
    print("Cold")


#Q.no.21

year = int(input("\nEnter a year: "))

if year % 100 == 0:
    print(year, "is a century year.")
else:
    print(year, "is not a century year.")


#Q.no.22

age = int(input("\nEnter your age: "))

if age < 12 or age > 60:
    print("Discount applies.")
else:
    print("No discount.")


#Q.no.23

experience = float(input("\nYears of Experience: "))
rating = float(input("Performance Rating (out of 10): "))

if experience > 2 and rating > 7:
    print("Bonus is awarded.")
else:
    print("No Bonus")


#Q.no.24

year = int(input("\nEnter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")


#Q.no.25

year = int(input("\nEnter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(True)
else:
    print(False)