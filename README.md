# 📝 Enhanced CLI To-Do List

A command-line to-do list application written in Python that helps you manage tasks efficiently. It supports adding, listing, editing, marking as done, and deleting tasks, all stored in a JSON file. Tasks are sorted by due date to help prioritize deadlines.

## 📦 Features

- ✅ Add new tasks with title, description, and due date
- 📋 List all tasks, automatically sorted by due date
- ✏️ Edit task details (title, description, due date, status)
- ✔️ Mark tasks as done
- ❌ Delete individual tasks or all tasks
- 💾 Automatically saves tasks to `tasks.json`

## 🖥️ How It Works

Upon running the script, you'll be greeted with a menu of options:
1. Add task  
2. List all tasks  
3. Mark a task as done  
4. Edit an existing task  
5. Delete an existing task  
6. Delete all tasks  
7. Exit

Tasks are saved in a JSON file named `tasks.json`. The app ensures dates are parsed and stored in a consistent format (`YYYY/MM/DD`).

## 📂 File Structure

```
project-folder/
│
├── tasks.json          # Automatically generated to store tasks
├── your_script.py      # Main Python file (rename as needed)
└── README.md           # Project documentation
```

## 🛠️ How to Run

```bash
python main.py
```

Make sure you're using Python 3.6 or higher.

## 🗒️ Date Format

The accepted date formats are:

- `YYYY/MM/DD`
- `YYYY-MM-DD`

If no valid date is provided, the task is added without a due date.

## 📌 Ideas for Future Improvements

- Export to CSV or HTML
- Add unit tests
- Integrate color output for better UI (colorama)
- adding priority
- sort by priority and due date(like first high(the high itself sorted by date) then medium and then low priority tasks)
- filter listing tasks by done and undone
- search feature
- refactor i/o and validation into function


## 🧠 Author

Made by SpaceJesus. Feel free to fork, improve, and contribute!
