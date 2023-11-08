# database.py will handle the database connection and provide a cursor and connection object that can be used by the repository.
import sqlite3


class Database:
    def __init__(self, database_name):
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()

        # Create the 'users' table if it doesn't exist
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT,
                username TEXT,
                password TEXT
            )
        """
        )

        # Create the 'todos(TaskList)' table if it doesn't exist
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY,
                task_description TEXT,
                priority int,
                completed INTEGER
            )
        """
        )
        self.conn.commit()
