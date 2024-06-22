# TO DO LIST

import os

class ToDoList: # Initialization
    def __init__(self):
        self.tasks = []

    def add_task(self, task): #Adding a Task
        self.tasks.append({'task': task, 'completed': False})
        print(f"Added task: {task}")

    def view_tasks(self): #Viewing Tasks
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                status = "Done" if task['completed'] else "Not Done"
                print(f"{i}. {task['task']} - {status}")

    def update_task(self, task_number, new_task):#updatetask
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]['task'] = new_task
            print(f"Updated task {task_number} to: {new_task}")
        else:
            print("Invalid task number.")

    def complete_task(self, task_number):#completingtask
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]['completed'] = True
            print(f"Marked task {task_number} as complete.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):#deletingtask
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Deleted task: {removed_task['task']}")
        else:
            print("Invalid task number.")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main(): #mainfuction
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. View tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Complete task")
        print("5. Delete task")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            clear_screen()
            todo_list.view_tasks()
        elif choice == '2':
            task = input("Enter the task: ").strip()
            todo_list.add_task(task)
        elif choice == '3':
            task_number = int(input("Enter task number to update: ").strip())
            new_task = input("Enter the new task: ").strip()
            todo_list.update_task(task_number, new_task)
        elif choice == '4':
            task_number = int(input("Enter task number to complete: ").strip())
            todo_list.complete_task(task_number)
        elif choice == '5':
            task_number = int(input("Enter task number to delete: ").strip())
            todo_list.delete_task(task_number)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
