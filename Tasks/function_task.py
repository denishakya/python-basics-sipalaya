# Write a Python function to find the maximum of three numbers.

def max_of_three(a, b, c):
    return max(a, b, c)

print("\nMaximum of Three Numbers:", max_of_three(8, 6, 5))



# Write a Python function to sum all the numbers in a list.

def sum_list(numbers):
    return sum(numbers)

a = [6, 5, 7, 3, 4]
print("\nList:", a)
print("Sum of all the numbers in a list: ", sum_list(a))



# Write a function that take list of string and show only string which are start with s

def s_strings(strings):
    return [s for s in strings if s.lower().startswith('s')]

a = ["Sujan", "Saroj", "Mahesh", "Arjun", "Sushant", "Bishal"]
print("\nList:", a)
print("List of String starting with 'S':", s_strings(a))



# Write a Python function to multiply all the numbers in a list

def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

a = [6, 5, 8, 7, 2]
print("\nList:", a)
print("Product of all the numbers in list:", multiply_list(a))



# Write a Python function to calculate the factorial of a number

def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
    
num1 = int(input("\nEnter any Number: "))
print(f"The factorial of {num1}:", factorial(num1))



# Write a Python function that takes a number as a parameter and checks whether the number is prime or not.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num1 = int(input("\nEnter any Number: "))
print(f"{num1} is a Prime Number:", is_prime(num1))



# Write a Python program to print the even numbers from a given list

def even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nList:", a)
print("Even Numbers:", even_numbers(a))


print(" ")