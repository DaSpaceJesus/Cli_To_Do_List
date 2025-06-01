import os
import json
from datetime import datetime

data_file = 'tasks.json'


def load_data():
    if os.path.exists(data_file):
        with open(data_file, 'r') as f:
            return json.load(f)
    else:
        tasks = [["Name", "Description", "Due Date", "Status"]]
        return tasks


def parse_date(date_str):
    formats = ["%Y/%m/%d", "%Y-%m-%d"]
    for format in formats:
        try:
            return datetime.strptime(date_str, format)
        except ValueError:
            continue
    raise ValueError(f"Date Format not recognized! Use one of {formats}")


def add_task(tasks):
    multiple = True
    while multiple:
        taskitem = []
        name = input("Enter task title: ")
        taskitem.append(name)
        description = input("Enter task description: ")
        taskitem.append(description)
        date = input("Enter task date(YYYY/MM/DD or YYYY-MM-DD): ")
        timeparse = ''
        if date:
            parsed = parse_date(date)
            timeparse = parsed.strftime("%Y/%m/%d")
        taskitem.append(timeparse)
        status = "Not Done"
        taskitem.append(status)
        tasks.append(taskitem)
        choice = int(input("Task added! Do want to add another task?\n 1. Yes\n 2. No\nYour choice: "))
        if choice == 2:
            multiple = False


def list_tasks(tasks):
    if len(tasks) < 2:
        print("No tasks found!")
    else:
        for row in tasks:
            print("{:<0} , {:<6}, {:<5}, {:<5}".format(*row))


def mark_done(tasks):
    if len(tasks) <= 1:
        print("No tasks left to mark done!")
        return tasks

    print("\nTasks:")
    for index, task in enumerate(tasks[1:], start=1):
        print(index, task)
    choice = int(input("Enter your choice: "))
    tasks[choice][3] = "Done"
    return tasks


def edit_task(tasks):
    print("\nWhich Task? :")
    for index, task in enumerate(tasks[1:], start=1):
        print(index, task)
    choice = int(input("Enter your choice: "))
    if choice > len(tasks) - 1:
        print("Invalid choice!")
        return tasks
    choice2 = int(
        input("What do you want to edit?\n 1. Name\n 2. Description\n 3. Due Date\n 4. Status\nYour choice: "))
    if choice2 == 1:
        tasks[choice][0] = input("Enter new task name: ")
    elif choice2 == 2:
        tasks[choice][1] = input("Enter new task description: ")
    elif choice2 == 3:
        tasks[choice][2] = input("Enter new task date: ")
    elif choice2 == 4:
        if tasks[choice][3] == "Not Done":
            tasks[choice][3] = "Done"
        elif tasks[choice][3] == "Done":
            tasks[choice][3] = "Not Done"
    return tasks


def delete_task(tasks):
    print("\nWhich Task? :")
    for index, task in enumerate(tasks[1:], start=1):
        print(index, task)
    choice = int(input("Enter your choice: "))
    tasks.pop(choice)
    print("Tasks deleted!")
    return tasks


def save_tasks(tasks):
    with open(data_file, 'w') as f:
        json.dump(tasks, f)
        print("Tasks Saved")


def delete_all():
    if os.path.exists(data_file):
        os.remove(data_file)
        print("Tasks Deleted")


def main():
    tasks = load_data()
    print("Welcome to Enhanced CLI To Do List!\n")
    stay = True
    while stay:
        print("What do you want to do?\n 1. Add task\n 2. List all tasks\n 3. Mark a task as done")
        choice1 = int(
            input(" 4. Edit an existing task\n 5. Delete an existing task\n 6. Delete all!\n 7. Exit\nYour Choice: "))
        if choice1 == 1:
            add_task(tasks)
            save_tasks(tasks)
            Continue = int(input("Continue?\n 1. Yes\n 2. No\nYour choice: "))
            if Continue == 2:
                stay = False

        elif choice1 == 2:
            list_tasks(tasks)
            Continue = int(input("Continue?\n 1. Yes\n 2. No\nYour choice: "))
            if Continue == 2:
                stay = False

        elif choice1 == 3:
            tasks = mark_done(tasks)
            save_tasks(tasks)
            Continue = int(input("Continue?\n 1. Yes\n 2. No\nYour choice: "))
            if Continue == 2:
                stay = False

        elif choice1 == 4:
            tasks = edit_task(tasks)
            save_tasks(tasks)
            Continue = int(input("Continue?\n 1. Yes\n 2. No\nYour choice: "))
            if Continue == 2:
                stay = False

        elif choice1 == 5:
            delete_task(tasks)
            save_tasks(tasks)
            Continue = int(input("Continue?\n 1. Yes\n 2. No\nYour choice: "))
            if Continue == 2:
                stay = False

        elif choice1 == 6:
            delete_all()
            stay = False

        elif choice1 == 7:
            print("Bye!")
            stay = False


if __name__ == '__main__':
    main()
