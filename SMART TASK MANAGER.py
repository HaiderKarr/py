import os 
def display_menu():
    print("SMART TASK MANAGER")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    return input("Choose an option: ")

def load_tasks(filename="tasks.txt"):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename,"w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")

def main():
    file_name = "my_private_tasks.txt"
    tasks = load_tasks(file_name)
    while True:
        choice = display_menu()
        if choice == "1":
            task = input("Enter a new task: ")
            tasks.append(task)
            save_tasks(tasks, file_name)
            print("Task added successfully!")
        elif choice == "2":
            print("Your Tasks:")
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")
        elif choice == "3":
            print("Your Tasks:")
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")
            try:
                task_num = int(input("Enter the task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    save_tasks(tasks, file_name)
                    print(f"Task '{removed_task}' deleted successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Exiting the Task Manager. Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()