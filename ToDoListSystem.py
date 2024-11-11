tasks = []

def display_menu():
    print("\nTo-Do List Manager")
    print("PHINMA COC CITE")
    print("-----------------------")
    print("1. Add a task")
    print("2. Edit a task")
    print("3. Delete a task")
    print("4. Mark task as completed")
    print("5. View pending tasks")
    print("6. View completed tasks")
    print("7. Exit")
    print("-------------------------")


def add_task():
    task_name = input("Enter task name: ")
    priority = input("Enter task priority (High, Medium, Low): ")
    deadline = input("Enter task deadline: ")
    task = {'name': task_name, 'priority': priority, 'deadline': deadline, 'completed': False}
    tasks.append(task)
    print(f'Task "{task_name}" added!')

def edit_task():
    task_id = int(input("Enter task number to edit: ")) - 1
    if 0 <= task_id < len(tasks):
        task_name = input("Enter new task name: ")
        priority = input("Enter new task priority (Top Priority, Med Priority , Low Priority): ")
        deadline = input("Enter new task deadlin: ")
        tasks[task_id]['name'] = task_name
        tasks[task_id]['priority'] = priority
        tasks[task_id]['deadline'] = deadline
        print(f'Task {task_id + 1} updated!')
    else:
        print("Invalid task number!")

def delete_task():
    task_id = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_id < len(tasks):
        removed_task = tasks.pop(task_id)
        print(f'Task "{removed_task["name"]}" deleted!')
    else:
        print("Invalid task number!")


def mark_completed():
    task_id = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = True
        print(f'Task "{tasks[task_id]["name"]}" marked as completed!')
    else:
        print("Invalid task number!")


def view_pending_tasks():
    print("\nPending Tasks:")
    for i, task in enumerate(tasks):
        if not task['completed']:
            print(f"{i + 1}. {task['name']} - Priority: {task['priority']} - Deadline: {task['deadline']}")
    print()

def view_completed_tasks():
    print("\nCompleted Tasks:")
    for i, task in enumerate(tasks):
        if task['completed']:
            print(f"{i + 1}. {task['name']}")
    print()


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            edit_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_completed()
        elif choice == "5":
            view_pending_tasks()
        elif choice == "6":
            view_completed_tasks()
        elif choice == "7":
            print("Exiting To-Do List Manager.")
            break
        else:
            print("Invalid choice! Please try again.")

main()
Write to GROUP 7 PROGRAMMING
