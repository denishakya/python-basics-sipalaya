print("")

# Task 1 
# Filter List by Skipping Names Starting with 'S'

a = ["sujan", "ram", "hari", "Syam", "Suman"]
b = []
for item in a:
    if item.lower().startswith("s"):
        continue
    b.append(item)
print(b)

print("")


# Task 2
# Print Multiplication Table of a Given Number

num = int(input("Enter any number: "))
a = 1
while a <= 10:
    print(f"{num} X {a} = {num * a}")
    a += 1

print("")


# Task 3
# Remove Common Elements from Two Lists

a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8]
op = []
for i in a:
    for j in b:
        if i == j:
            a.remove(i)
            b.remove(j)
print(a+b)



# Find the Second Largest Number Using While Loops
# input = [45, 12, 10, 25, 78, 56, 20, 4, 45, 99]
# output = 78

numbers = [45, 12, 10, 25, 78, 56, 20, 4, 45, 99]

print("\nNumbers: ", numbers)

i = 0
num = len(numbers)

while i < num:
    j = i + 1
    while j < num:
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
        j += 1
    i += 1
print("Ascending Order: ", numbers)
print("Second Largest: ", numbers[-2])


# Find the Second Largest Number Using For Loops
# input = [45, 12, 10, 25, 78, 56, 20, 4, 45, 99]
# output = 78

numbers = [45, 12, 10, 25, 78, 56, 20, 4, 45, 99]

print("\nNumbers: ", numbers)

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print("Ascending Order: ", numbers)
print("Second Largest: ", numbers[-2])


# write a program to display all prime number within an interval
# start=10
# end=20
# output=[11,13,17,19]

start = 10
end = 20

print(f"\nPrime Numbers between {start} and {end} :")

for num in range(start, end+1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime == True:
            print(num, end=" ")