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
        parsed = parse_date(date)
        taskitem.append(parsed.strftime("%Y/%m/%d"))
        status = "Not Done"
        taskitem.append(status)
        tasks.append(taskitem)
        choice = int(input("Task added! Do want to add another task?\n 1. Yes\n 2. No\nYour choice: "))
        if choice == 2:
            multiple = False



def list_tasks(tasks):
    for row in tasks:
        print("{:<5} , {:<10}, {:<15}, {:<20}".format(*row))

def save_tasks(tasks):
    with open(data_file, 'w') as f:
        json.dump(tasks, f)
        print("Tasks Saved")

def mark_done(tasks):
    if len(tasks) <= 1:
        print("No tasks left to mark done!")
        return

    list_tasks(tasks)
    name = str(input("Enter the name of the task that you want to be marked as done: "))
    if name != "Name":
        for task in tasks:
            if task[0] == name:
                task[3] = "Done"
    else:
        print("Wrong!")
    return tasks




def main():
    tasks = load_data()
    stay = True
    while stay:
        print("What do you want to do?\n 1. Add task\n 2. List all tasks\n 3. Mark a task as done")
        choice1 = int(input(" 4. Edit an existing task\n 5. Delete an existing task\n 6. Exit\nYour Choice: "))
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
            tasks= mark_done(tasks)
            save_tasks(tasks)
            #Continue = int(input("Continue?\n 1. Yes\n 2. No\nYour choice: "))
            #if Continue == 2:
            stay = False
        elif choice1 == 6:
            stay = False





if __name__ == '__main__':
    main()


