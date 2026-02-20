def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")

def view_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task.strip()}")
    except:
        print("No tasks found.")

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
