# Project 1: simple To-Do List 
# Create a basic command-line to-do list application using python lists and  data types 
# Implement functionality to add,remove, and view tasks 

def todo_list_app():
    tasks = []

    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter new task: ")
            tasks.append(task)
            print("Task added!")

        elif choice == "2":
            task = input("Enter task to remove: ")
            if task in tasks:
                tasks.remove(task)
                print("Task removed!")
            else:
                print("Task not found!")

        elif choice == "3":
            print("\nYour Tasks:")
            if not tasks:
                print("No tasks available.")
            else:
                for i, t in enumerate(tasks, start=1):
                    print(f"{i}. {t}")

        elif choice == "4":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")