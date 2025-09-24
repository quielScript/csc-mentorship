import os
from os import mkdir

FILE_PATH = "tasks.txt"

# w - write (override/delete previous records)
# a - append (adds a new item at the end of the file)
def add_task(task):
    if not os.path.exists(FILE_PATH):
        print("File not found. Creating a new one...")
        with open(FILE_PATH, "w") as file:
            pass  # creates an empty file
    else:
        print("File already exists!")

    # open(file location, mode)
    with open(FILE_PATH, "a") as file:
        file.write(f"{task}\n")
    print("Task added!")

# r - read
def view_tasks():
    if not os.path.exists(FILE_PATH):
        print("File not found. Creating a new one...")
        with open(FILE_PATH, "w") as file:
            pass  # creates an empty file
    else:
        print("File already exists!")

    print("===Tasks===")
    with open(FILE_PATH, "r") as file:
        # ["eat", "sleep", "study"]
        tasks = file.readlines()

        if not tasks:
            print("No tasks found!")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")

def update_task(task_num):
    if not os.path.exists(FILE_PATH):
        print("File not found. Creating a new one...")
        with open(FILE_PATH, "w") as file:
            pass  # creates an empty file
    else:
        print("File already exists!")

    tasks = []
    with open(FILE_PATH, "r") as file:
        tasks = file.readlines()

        # Guard clause
        if  task_num < 1 or task_num > len(tasks):
            print("Task number does not exists!")
            return

        if not tasks:
            print("No tasks found!")
        else:
            new_task = input("Enter a new task: ")
            tasks[task_num - 1] = new_task + "\n"

    with open(FILE_PATH, "w") as file:
        file.writelines(tasks)

    print("Updated!")

def delete_task(task_num):
    if not os.path.exists(FILE_PATH):
        print("File not found. Creating a new one...")
        with open(FILE_PATH, "w") as file:
            pass  # creates an empty file
    else:
        print("File already exists!")

    tasks = []
    with open(FILE_PATH, "r") as file:
        tasks = file.readlines()

        # Guard clause
        if task_num < 1 or task_num > len(tasks):
            print("Task number does not exists!")
            return

        if not tasks:
            print("No tasks found!")
        else:
            del tasks[task_num - 1]

    with open(FILE_PATH, "w") as file:
        file.writelines(tasks)
    print("Deleted!")

while True:
    print("""
Enter option:
1. Add task
2. View tasks
3. Update task
4. Delete task
5. Exit
    """)

    try:
        option = int(input("Enter option (1-5): "))

        if option == 1:
            task = input("Enter task: ")
            add_task(task)
        elif option == 2:
            view_tasks()
        elif option == 3:
            view_tasks()
            task_num = int(input("Enter task number to update: "))
            update_task(task_num)
        elif option == 4:
            view_tasks()
            task_num = int(input("Enter task number to delete: "))
            delete_task(task_num)
        elif option == 5:
            break;
        else:
            print("Invalid option. Please try again!")
    except ValueError:
        print("Invalid option. Please try again!")