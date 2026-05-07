# Project: Advanced To-Do List Manager
# Student: Asma Umar | Institute: As-Sa’adah Institute

class TodoListManager:
    def __init__(self):
        self.weekly_tasks = []
        self.monthly_tasks = []

    def add_weekly_task(self, task):
        if task and isinstance(task, str):
            self.weekly_tasks.append(task.strip())
            print(f"Added weekly task: '{task}'")
        else:
            print("Invalid task. Please enter a valid text.")

    def add_monthly_task(self, task):
        if task and isinstance(task, str):
            self.monthly_tasks.append(task.strip())
            print(f"Added monthly task: '{task}'")
        else:
            print("Invalid task.")

    def view_tasks(self):
        print("\n--- YOUR TASK SUMMARY ---")
        print("Weekly:", self.weekly_tasks if self.weekly_tasks else "Empty")
        print("Monthly:", self.monthly_tasks if self.monthly_tasks else "Empty")
        print("--------------------------")

# --- Main Program Execution ---
manager = TodoListManager()

print("Welcome! Type 'done' to finish adding tasks.")

# Loop for Weekly Tasks
while True:
    task_input = input("Enter a Weekly Task: ")
    if task_input.lower() == 'done':
        break
    manager.add_weekly_task(task_input)

# Loop for Monthly Tasks
while True:
    task_input = input("Enter a Monthly Task: ")
    if task_input.lower() == 'done':
        break
    manager.add_monthly_task(task_input)

# Final Output
manager.view_tasks()
