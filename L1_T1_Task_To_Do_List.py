import json

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})

    def view_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{index}. {task['task']} - {status}")

    def mark_task_as_done(self, index):
        if 0 < index <= len(self.tasks):
            self.tasks[index - 1]["done"] = True
        else:
            print("Invalid task index")

    def delete_task(self, index):
        if 0 < index <= len(self.tasks):
            del self.tasks[index - 1]
        else:
            print("Invalid task index")

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            json.dump(self.tasks, file)

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            pass 

def main():
    todo_list = ToDoList()

    # Load tasks from file if it exists
    todo_list.load_from_file("todo.json")

    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Save and Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            index = int(input("Enter task index to mark as done: "))
            todo_list.mark_task_as_done(index)
        elif choice == "4":
            index = int(input("Enter task index to delete: "))
            todo_list.delete_task(index)
        elif choice == "5":
            todo_list.save_to_file("todo.json")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
