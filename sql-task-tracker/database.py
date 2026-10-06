# database.py
# CSE310 Module 3 - SQL Task Tracker
# Author: Mike Okello
# Purpose: Handles all database operations with 2 relational tables

import sqlite3
from datetime import datetime

DATABASE_NAME = "task_tracker.db"

def get_connection():
    """Create and return a database connection with foreign keys enabled."""
    conn = sqlite3.connect(DATABASE_NAME)
    conn.execute("PRAGMA foreign_keys = ON") # Enforce foreign key relationships
    return conn

def create_tables():
    """Create Categories and Tasks tables with primary and foreign keys."""
    conn = get_connection()
    cursor = conn.cursor()

    # Create Categories table - Parent table
    # Unique requirement: Primary Key and Unique constraint
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Categories (
            category_id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name TEXT NOT NULL UNIQUE,
            description TEXT NOT NULL
        )
    """)

    # Create Tasks table - Child table with Foreign Key
    # Unique requirement: Foreign Key referencing Categories
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Tasks (
            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            priority TEXT CHECK(priority IN ('Low', 'Medium', 'High')) NOT NULL,
            status TEXT CHECK(status IN ('Pending', 'In Progress', 'Completed')) NOT NULL DEFAULT 'Pending',
            due_date TEXT,
            category_id INTEGER NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE CASCADE
        )
    """)

    conn.commit()
    conn.close()
    print("Tables created successfully.")

# --- CREATE Operations ---

def add_category(name, description):
    """Insert a new category into Categories table."""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO Categories (category_name, description) VALUES (?,?)",
            (name, description)
        )
        conn.commit()
        print(f"Category '{name}' added.")
        return cursor.lastrowid
    except sqlite3.IntegrityError:
        print(f"Error: Category '{name}' already exists.")
        return None
    finally:
        conn.close()

def add_task(title, description, priority, status, due_date, category_id):
    """Insert a new task linked to a category."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Tasks (title, description, priority, status, due_date, category_id)
        VALUES (?,?,?,?,?,?)
    """, (title, description, priority, status, due_date, category_id))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    print(f"Task '{title}' added with ID {task_id}.")
    return task_id

# --- READ Operations with JOIN (Unique Requirement) ---

def get_all_tasks_with_category():
    """Read all tasks using JOIN to show category name - UNIQUE REQUIREMENT: JOIN query."""
    conn = get_connection()
    cursor = conn.cursor()
    # Using INNER JOIN to combine Tasks and Categories
    cursor.execute("""
        SELECT Tasks.task_id, Tasks.title, Tasks.priority, Tasks.status,
               Tasks.due_date, Categories.category_name, Categories.description as cat_desc
        FROM Tasks
        INNER JOIN Categories ON Tasks.category_id = Categories.category_id
        ORDER BY Tasks.priority DESC, Tasks.due_date
    """)
    results = cursor.fetchall()
    conn.close()
    return results

def get_tasks_by_category(category_name):
    """Filter tasks by category name using JOIN."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT Tasks.title, Tasks.status, Tasks.priority
        FROM Tasks
        JOIN Categories ON Tasks.category_id = Categories.category_id
        WHERE Categories.category_name =?
    """, (category_name,))
    results = cursor.fetchall()
    conn.close()
    return results

def get_all_categories():
    """Get all categories."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Categories")
    results = cursor.fetchall()
    conn.close()
    return results

# --- UPDATE Operations ---

def update_task_status(task_id, new_status):
    """Update task status by ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Tasks SET status =? WHERE task_id =?",
        (new_status, task_id)
    )
    conn.commit()
    conn.close()
    print(f"Task {task_id} updated to {new_status}.")

def update_task_priority(task_id, new_priority):
    """Update task priority."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Tasks SET priority =? WHERE task_id =?",
        (new_priority, task_id)
    )
    conn.commit()
    conn.close()

# --- DELETE Operations ---

def delete_task(task_id):
    """Delete a task by ID - UNIQUE REQUIREMENT: DELETE."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Tasks WHERE task_id =?", (task_id,))
    conn.commit()
    conn.close()
    print(f"Task {task_id} deleted.")

def delete_category(category_id):
    """Delete a category - will cascade delete tasks due to ON DELETE CASCADE."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Categories WHERE category_id =?", (category_id,))
    conn.commit()
    conn.close()
    print(f"Category {category_id} deleted.")

def clear_all_data():
    """Clear all data for testing - useful for demo."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Tasks")
    cursor.execute("DELETE FROM Categories")
    conn.commit()
    conn.close()