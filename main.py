import os
import json
from datetime import datetime

data_file = 'tasks.json'

def parse_date(date_str):
    formats = ["%Y/%m/%d", "%Y-%m-%d"]
    for format in formats:
        try:
            return datetime.strptime(date_str, format)
        except ValueError:
            continue
    raise ValueError(f"Date Format not recognized! Use one of {formats}")

def load_data():
    if os.path.exists(data_file):
        with open(data_file, 'r') as f:
            return json.load(f)
    else:
        tasks = []
        return tasks

def add_task(tasks):
    taskitem = []
    name = input("Enter task title: ")
    taskitem.append(name)
    description = input("Enter task description: ")
    taskitem.append(description)
    date = input("Enter task date(YYYY/MM/DD or YYYY-MM-DD): ")
    parsed = parse_date(date)
    taskitem.append(parsed)
    tasks.append(taskitem)

def list_tasks():
    none



def main():
    tasks = load_data()
    print("What do you want to do?\n 1. Add task\n 2. List all tasks\n 3. Mark a task as done")
    choice1 = int(input(" 4. Edit an existing task\n 5. Delete an existing task\nYour Choice: "))
    if choice1 == 1:
        add_task(tasks)
    print(tasks)





if __name__ == '__main__':
    main()


