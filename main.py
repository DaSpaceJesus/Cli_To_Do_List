def add_task(tasks):
    name = input("Enter task title: ")
    tasks.append(name)
    description = input("Enter task description: ")
    tasks.append(description)
    date = input("Enter task date(YYYYMMDD): ")
    tasks.append(date)



def main():
    tasks = []
    print("What do you want to do?\n 1. Add task\n 2. List all tasks\n 3. Mark a task as done")
    choice1 = int(input(" 4. Edit an existing task\n 5. Delete an existing task\nYour Choice: "))
    if choice1 == 1:
        add_task(tasks)
    print(tasks)





if __name__ == '__main__':
    main()


