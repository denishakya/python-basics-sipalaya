# Project 1: simple To-Do List 
# o Create a basic command-line to-do list application using python lists and  data types 
# o Implement functionality to add,remove, and view tasks 

def todo_list():
    tasks = []

    while True:
        print("\n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
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
            print("Tasks:", tasks)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")
