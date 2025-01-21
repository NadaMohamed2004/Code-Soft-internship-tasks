import sys

todo_list = []

def display_menu():
    """Displays the menu options."""
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    """Adds a new task to the to-do list."""
    task = input("\nEnter a new task: ")
    todo_list.append(task)
    print(f"\"{task}\" has been added to your to-do list.")

def view_tasks():
    """Displays all tasks."""
    if not todo_list:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for id, task in enumerate(todo_list, start=1):
            print(f"{id}. {task}")


def update_task():
    """Updates an existing task."""
    view_tasks()
    if todo_list:
        try:
            task_number = int(input("\nEnter the task number to update: "))
            if 1 <= task_number <= len(todo_list):
                new_task = input("Enter the updated task: ")
                todo_list[task_number - 1] = new_task
                print(f"Task {task_number} has been updated to \"{new_task}\".")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task():
    """Deletes a task from the to-do list."""
    view_tasks()
    if todo_list:
        try:
            task_number = int(input("\nEnter the task number to delete: "))
            if 1 <= task_number <= len(todo_list):
                removed_task = todo_list.pop(task_number - 1)
                print(f"\"{removed_task}\" has been removed from your to-do list.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("enter a valid number.")

def main():
    """Main function to run the application."""
    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                add_task()
                
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                update_task()
            elif choice == 4:
                delete_task()
            elif choice == 5:
                print("\nGoodbye! ")
                sys.exit()
            else:
                print("Invalid choice. Please choose a number between 1 and 5.")
        except ValueError:
            print("enter a valid number.")

if __name__ == "__main__":
    main()
