def display_menu():
    # Display the main menu options
    print("\n--- TO-DO List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_task(tasks):
    # Show current tasks or indicate if list is empty
    if not tasks:
        print("Your TO-DO List is empty!")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    # Prompt user to add a new task
    task = input("Enter a task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added successfully.")
    else:
        print("Empty task cannot be added.")

def remove_task(tasks):
    # Show tasks and ask which one to remove
    view_task(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Task '{removed}' has been removed successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid integer number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter an option (1-4): ").strip()
        if choice == "1":
            view_task(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please enter a valid option (1-4).")

if __name__ == "__main__":
    main()
