# 📝 Task Manager

A simple terminal-based Task Manager built with Python and MySQL.

Users can:
- Add tasks
- View all tasks
- Mark tasks as done
- Delete tasks

##  Technologies
- Python 3
- MySQL
- MySQL Connector for Python (`mysql-connector-python`)

##  Setup Instructions

1. **Create the MySQL database:**

```sql
CREATE DATABASE task_db;

USE task_db;

CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    done BOOLEAN DEFAULT FALSE
);
