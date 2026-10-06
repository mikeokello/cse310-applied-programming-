# main.py
# CSE310 Module 3 - SQL Task Tracker Main Application
# Author: Mike Okello
# This file provides user interface and demonstrates all CRUD operations

import database

def print_menu():
    """Display main menu options."""
    print("\n=== SQL TASK TRACKER - Module 3 ===")
    print("1. Add Category")
    print("2. Add Task")
    print("3. View All Tasks (with JOIN)")
    print("4. View Tasks by Category")
    print("5. Update Task Status")
    print("6. Delete Task")
    print("7. View All Categories")
    print("8. Seed Sample Data")
    print("9. Exit")

def seed_data():
    """Insert sample data to demonstrate relational database - REQUIRED for video demo."""
    # Clear existing data
    database.clear_all_data()

    # Add Categories - Parent records
    work_id = database.add_category("Work", "Work related tasks and projects")
    school_id = database.add_category("School", "CSE310 and university assignments")
    personal_id = database.add_category("Personal", "Personal life and home tasks")

    # Add Tasks - Child records linked via foreign key
    database.add_task("Complete Module 3", "Finish SQL Task Tracker project", "High", "In Progress", "2026-10-10", school_id)
    database.add_task("Prepare Presentation", "Create PowerPoint for work meeting", "Medium", "Pending", "2026-10-12", work_id)
    database.add_task("Buy Groceries", "Milk, bread, eggs", "Low", "Pending", "2026-10-08", personal_id)
    database.add_task("Study for Exam", "Review SQL JOINs and Foreign Keys", "High", "Pending", "2026-10-09", school_id)
    database.add_task("Fix Bug in App", "Debug task tracker delete function", "High", "Completed", "2026-10-07", work_id)

    print("\nSample data seeded successfully with 3 categories and 5 tasks!")

def main():
    """Main program loop that handles user interaction."""
    # Initialize database tables
    database.create_tables()
    print("Welcome to SQL Task Tracker!")

    # Auto-seed if empty for first run
    cats = database.get_all_categories()
    if not cats:
        seed_data()

    while True:
        print_menu()
        choice = input("Enter your choice (1-9): ").strip()

        if choice == "1":
            # CREATE Category
            name = input("Category name: ")
            desc = input("Category description: ")
            database.add_category(name, desc)

        elif choice == "2":
            # CREATE Task
            title = input("Task title: ")
            desc = input("Task description: ")
            priority = input("Priority (Low/Medium/High): ").capitalize()
            status = input("Status (Pending/In Progress/Completed): ").title()
            due = input("Due date (YYYY-MM-DD): ")
            print("Available Categories:")
            for cat in database.get_all_categories():
                print(f" {cat[0]}: {cat[1]}")
            cat_id = int(input("Enter category ID: "))
            database.add_task(title, desc, priority, status, due, cat_id)

        elif choice == "3":
            # READ with JOIN - Main unique requirement demonstration
            print("\n--- All Tasks with Categories (JOIN Query) ---")
            tasks = database.get_all_tasks_with_category()
            if not tasks:
                print("No tasks found.")
            for task in tasks:
                # task = (task_id, title, priority, status, due_date, category_name, cat_desc)
                print(f"[{task[0]}] {task[1]} | {task[2]} | {task[3]} | Due: {task[4]} | Category: {task[5]}")

        elif choice == "4":
            # READ filtered by category
            cat_name = input("Enter category name to filter (Work/School/Personal): ")
            tasks = database.get_tasks_by_category(cat_name)
            print(f"\n--- Tasks in Category: {cat_name} ---")
            for t in tasks:
                print(f"- {t[0]} | Status: {t[1]} | Priority: {t[2]}")

        elif choice == "5":
            # UPDATE
            task_id = int(input("Enter task ID to update: "))
            new_status = input("New status (Pending/In Progress/Completed): ").title()
            database.update_task_status(task_id, new_status)

        elif choice == "6":
            # DELETE
            task_id = int(input("Enter task ID to delete: "))
            database.delete_task(task_id)

        elif choice == "7":
            # READ Categories
            print("\n--- Categories ---")
            for cat in database.get_all_categories():
                print(f"ID: {cat[0]} | Name: {cat[1]} | Desc: {cat[2]}")

        elif choice == "8":
            seed_data()

        elif choice == "9":
            print("Exiting Task Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()