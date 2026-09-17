"""
CSE 310 Module #1 - To-Do Manager
Author: Mike Okello
Description: A cloud-ready to-do manager that stores tasks in JSON database.
This demonstrates continuous improvement with small steps.
"""

import json
import os
from datetime import datetime

DATA_FILE = "tasks.json"

def load_tasks():
    """Load tasks from JSON file, return empty list if file not found."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            return data
    except (json.JSONDecodeError, FileNotFoundError):
        print("Warning: Could not load tasks, starting fresh.")
        return []

def save_tasks(tasks):
    """Save tasks list to JSON file with pretty formatting."""
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(tasks, f, indent=4)
        print(f"Tasks saved successfully to {DATA_FILE}")
    except Exception as e:
        print(f"Error saving tasks: {e}")

def add_task(tasks):
    """Prompt user to add a new task with title and priority."""
    title = input("Enter task title: ").strip()
    if not title:
        print("Title cannot be empty!")
        return
    
    print("Priorities: 1=High, 2=Medium, 3=Low")
    priority = input("Enter priority (1-3): ").strip()
    if priority not in ["1", "2", "3"]:
        priority = "2"
    
    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "priority": int(priority),
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{title}' added!")

def view_tasks(tasks):
    """Display all tasks sorted by priority and completion status."""
    if not tasks:
        print("No tasks found. Add some tasks first!")
        return
    
    # Sort by priority (1 high first) and then by id
    sorted_tasks = sorted(tasks, key=lambda x: (x["completed"], x["priority"]))
    
    print("\n" + "="*50)
    print("YOUR TASKS")
    print("="*50)
    for task in sorted_tasks:
        status = "DONE" if task["completed"] else "TODO"
        prio_map = {1: "HIGH", 2: "MED", 3: "LOW"}
        prio = prio_map.get(task["priority"], "MED")
        print(f"[{task['id']}] {status} | {prio} | {task['title']} | Created: {task['created_at']}")
    print("="*50 + "\n")

def complete_task(tasks):
    """Mark a task as completed by ID."""
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        task_id = int(input("Enter task ID to mark complete: "))
        for task in tasks:
            if task["id"] == task_id:
                if task["completed"]:
                    print("Task already completed!")
                else:
                    task["completed"] = True
                    save_tasks(tasks)
                    print(f"Task {task_id} marked complete!")
                return
        print(f"Task ID {task_id} not found.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    """Delete a task by ID and re-index remaining tasks."""
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        task_id = int(input("Enter task ID to delete: "))
        original_len = len(tasks)
        tasks[:] = [t for t in tasks if t["id"] != task_id]
        
        # Re-index IDs to keep them sequential
        for index, task in enumerate(tasks, start=1):
            task["id"] = index
        
        if len(tasks) < original_len:
            save_tasks(tasks)
            print(f"Task {task_id} deleted and IDs re-indexed.")
        else:
            print(f"Task ID {task_id} not found.")
    except ValueError:
        print("Please enter a valid number.")

def show_stats(tasks):
    """Show statistics about tasks - demonstrates data analysis."""
    total = len(tasks)
    completed = sum(1 for t in tasks if t["completed"])
    pending = total - completed
    
    print("\n--- TASK STATISTICS ---")
    print(f"Total tasks: {total}")
    print(f"Completed: {completed}")
    print(f"Pending: {pending}")
    if total > 0:
        print(f"Completion rate: {(completed/total*100):.1f}%")
    print("-----------------------\n")

def main():
    """Main program loop - menu driven interface."""
    print("Welcome to CSE 310 To-Do Manager - Kaizen Edition!")
    print("Improve 1% daily with small tasks.")
    
    tasks = load_tasks()
    
    while True:
        print("\nMENU:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Show Stats")
        print("6. Exit")
        
        choice = input("Choose (1-6): ").strip()
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            show_stats(tasks)
        elif choice == "6":
            print("Keep improving small steps daily! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-6.")

if __name__ == "__main__":
    main()