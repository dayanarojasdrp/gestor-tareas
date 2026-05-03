
# Task Manager CLI

A Python-based Command Line Interface (CLI) application to manage personal tasks.  
This project demonstrates core programming concepts, including object-oriented design, error handling, file persistence, and modular code organization.

## Features
- Add new tasks
- List all tasks
- Mark tasks as completed
- Interactive menu in the terminal
- JSON file persistence (tasks are saved automatically)

## Project Structure
```
gestor-tareas/
 ├── main.py          # Entry point with interactive menu
 ├── tarea.py         # Task class definition
 ├── gestor.py        # Task manager class
 ├── tareas.json      # Auto-generated file storing tasks
 └── README.md        # Project documentation
```

## Installation
Clone the repository and navigate into the project folder:
```bash
git clone https://github.com/dayanarojasdrp/gestor-tareas.git
cd gestor-tareas
```

## Usage
Run the program with:
```bash
python3 main.py
```

Example interaction:
```
--- Task Manager ---
1. Add task
2. List tasks
3. Complete task
4. Exit
```

## Future Improvements
- Add deadlines and priorities
- Search and filter tasks
- Export tasks to CSV
- Unit tests for reliability

```
