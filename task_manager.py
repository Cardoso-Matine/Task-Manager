import mysql.connector


def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  
        database="task_db"
    )


def add_task():
    title = input("Enter task title: ")

    try:
        connection = connect()
        cursor = connection.cursor()
        query = "INSERT INTO tasks (title) VALUES (%s)"
        cursor.execute(query, (title,))
        connection.commit()
        print(" Task added!")
    except Exception as e:
        print(" Error:", e)
    finally:
        cursor.close()
        connection.close()


def list_tasks():
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tasks")
        results = cursor.fetchall()

        print("\n Task List:")
        print("-" * 40)
        for task in results:
            status = "" if task[2] else ""
            print(f"ID: {task[0]} | Title: {task[1]} | Done: {status}")
    except Exception as e:
        print(" Error:", e)
    finally:
        cursor.close()
        connection.close()


def mark_done():
    task_id = input("Enter task ID to mark as done: ")
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("UPDATE tasks SET done = TRUE WHERE id = %s", (task_id,))
        connection.commit()
        print(" Task marked as done!")
    except Exception as e:
        print(" Error:", e)
    finally:
        cursor.close()
        connection.close()


def delete_task():
    task_id = input("Enter task ID to delete: ")
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        connection.commit()
        print(" Task deleted.")
    except Exception as e:
        print(" Error:", e)
    finally:
        cursor.close()
        connection.close()


def main():
    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("0. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "0":
            print(" Exiting...")
            break
        else:
            print(" Invalid option. Try again.")

if __name__ == "__main__":
    main()
