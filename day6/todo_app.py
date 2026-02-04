# =====================================
# DAY 6: FILE HANDLING PROJECT
# MINI PROJECT: TO-DO APP (File Storage)
# =====================================

def show_menu():
    print("\n=== TO-DO MENU ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Exit")


def view_tasks():
    try:
        file = open("tasks.txt", "r")
        tasks = file.readlines()
        file.close()

        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(i, "-", task.strip())

    except FileNotFoundError:
        print("No tasks file found. Add a task first.")


def add_task():
    task = input("Enter new task: ")
    file = open("tasks.txt", "a")
    file.write(task + "\n")
    file.close()
    print("Task added successfully!")


# ===== MAIN PROGRAM =====

while True:
    show_menu()
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice. Try again.")