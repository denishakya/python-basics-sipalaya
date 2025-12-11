# Project1 :Multiplication table generator 
# o Using break ,continue and pass statements in loop 
# o Syntax and examples of control statements 

def multiplication_table():
    n = int(input("Enter a number: "))

    for i in range(1, 11):
        if i == 5:
            print("Skipping 5")  # example of continue
            continue
        if i == 8:
            print("Stopping at 8")  # example of break
            break
        print(f"{n} x {i} = {n*i}")
