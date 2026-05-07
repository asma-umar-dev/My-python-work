# Project: To-Do List Management System
# Student: Asma Umar | Institute: As-Sa’adah Institute

# Creating an empty list to store tasks
tasks = []

print("--- Simple To-Do List Manager ---")

# Adding tasks using input
print("Enter 3 main tasks for your day:")
task1 = input("1. ")
task2 = input("2. ")
task3 = input("3. ")

# Appending tasks to the list
tasks.append(task1)
tasks.append(task2)
tasks.append(task3)

print("\n" + "-" * 25)
print("Your Tasks for Today:")
# Displaying the list
print(f"Task List: {tasks}")
print("-" * 25)

# Example of removing a task (Optional logic)
status = input("\nDid you finish the first task? (yes/no): ").lower()
if status == "yes":
    removed_task = tasks.pop(0)
    print(f"Great! '{removed_task}' has been removed from the list.")
    print(f"Remaining Tasks: {tasks}")
else:
    print("Keep working on it! You can do it.")

print("\n--- Plan Updated Successfully ---")
