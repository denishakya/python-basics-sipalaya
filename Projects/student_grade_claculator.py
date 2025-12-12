# Project 2 : Student grade calculate  
# o Create a dictionary representing a student’s grades in different subjects and then calculates the student’s average grade 

def student_grade_calculator():
    grades = {
        "Math": 85,
        "Science": 90,
        "English": 78,
        "Computer": 92
    }

    total = sum(grades.values())
    average = total / len(grades)

    print("Student Grades:", grades)
    print("Average Grade:", round(average, 2))