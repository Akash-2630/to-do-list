import json
import os

# File to store the to-do list
TODO_FILE = 'todo_list.json'

# Load existing tasks from the JSON file
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

# Save tasks to the JSON file
def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file)

# Add a new task
def add_task(tasks, task):
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task "{task}" added!')

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Remove a task
def remove_task(tasks, task_number):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f'Task "{removed_task}" removed!')
    else:
        print("Invalid task number.")

# Main function to run the application
def main():
    tasks = load_tasks()
    
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            task_number = int(input("Enter the task number to remove: "))
            remove_task(tasks, task_number)
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()