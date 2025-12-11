# Project: Student grade Calculator 
# - Create a command-line program that calculates the grade of a student based on their test score 
# - Ask the user for their test score and display their grade (A,B,C,D,E, F) 

def grade_calculator():
    score = float(input("Enter your test score (0-100): "))

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    elif score >= 50:
        grade = "E"
    else:
        grade = "F"

    print(f"Your grade is: {grade}")
