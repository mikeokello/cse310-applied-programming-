# SQL Task Tracker - CSE310 Module 3

## Overview
This software is a **SQL Relational Database Task Tracker**. It manages tasks and categories using two related tables with foreign key relationships.

**Purpose:** To demonstrate SQL relational database concepts including primary keys, foreign keys, JOIN queries, and full CRUD operations (Create, Read, Update, Delete). This project helps users organize tasks by category (Work, School, Personal) with priorities and statuses.

I wrote this software to fulfill Module 3 requirements and to learn how relational databases work in real applications.

[Software Demo Video - Add your Zoom link here - 4-5 mins showing face + demo + code walkthrough]

## Relational Database
I used **SQLite** with Python's `sqlite3` module. SQLite is a lightweight relational database perfect for this module.

**Structure:**
- **Categories Table (Parent):** `category_id` (PK, AUTOINCREMENT), `category_name` (UNIQUE, NOT NULL), `description`
- **Tasks Table (Child):** `task_id` (PK), `title`, `description`, `priority` (CHECK constraint), `status` (CHECK), `due_date`, `category_id` (FK REFERENCES Categories ON DELETE CASCADE), `created_at`

**Relationships:**
- One Category can have MANY Tasks (One-to-Many)
- Foreign Key enforces integrity - cannot add task with invalid category_id

## Development Environment
- **Language:** Python 3.12
- **Database:** SQLite 3
- **Libraries:** sqlite3 (built-in), datetime
- **Tools:** VS Code, Git, GitHub, Zoom for recording

## Useful Websites
- [SQLite Foreign Key Support](https://www.sqlite.org/foreignkeys.html)
- [W3Schools SQL JOIN](https://www.w3schools.com/sql/sql_join.asp)
- [Python sqlite3 Documentation](https://docs.python.org/3/library/sqlite3.html)
- [BYU CSE310 Module Descriptions](https://byu.instructure.com)

## Future Work
- Add due date reminders and notifications
- Implement many-to-many relationship with Tags table
- Add user authentication with Users table
- Create GUI with Tkinter or web interface with Flask
- Add reports: tasks per category statistics

## How to Run
1. Clone repo: `git clone https://github.com/mikeokello/cse310-applied-programming-.git`
2. Go to folder: `cd sql-task-tracker`
3. Run: `python main.py`
4. Choose option 8 to seed sample data, then option 3 to see JOIN query results