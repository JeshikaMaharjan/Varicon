from database import Database


class UserRepository:
    def __init__(self, database_name):
        self.db = Database(database_name)


class TodoRepository:
    def __init__(self, database_name):
        self.db = Database(database_name)


class UserRepositoryImpl(UserRepository):
    def create(self, name, email, username, password):
        self.db.cursor.execute(
            "INSERT INTO users (name, email, username, password) VALUES (?,?,?, ?)",
            (name, email, username, password),
        )
        self.db.conn.commit()
        return self.db.cursor.lastrowid

    def get(self, user_id):
        self.db.cursor.execute(
            "SELECT id, name, email,username, password FROM users WHERE id = ?",
            (user_id,),
        )
        return self.db.cursor.fetchone()

    def get_by_username(self, username):
        self.db.cursor.execute(
            "SELECT id, username, password FROM users WHERE username = ?", (username,)
        )
        return self.db.cursor.fetchone()

    def update(self, user_id, updated_data):
        update_query = "UPDATE users SET {} WHERE id = ?".format(
            ", ".join(f"{key} = ?" for key in updated_data.keys())
        )
        values = list(updated_data.values())
        values.append(user_id)
        self.db.cursor.execute(update_query, values)
        self.db.conn.commit()
        return self.db.cursor.rowcount > 0

    def delete(self, user_id):
        self.db.cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        self.db.conn.commit()
        return self.db.cursor.rowcount > 0


class TodoRepositoryImpl(TodoRepository):
    def create(self, task_description, priority):
        self.db.cursor.execute(
            "INSERT INTO todos (task_description, priority,completed) VALUES (?, ?, 0)",
            (task_description, priority),
        )
        self.db.conn.commit()
        return self.db.cursor.lastrowid

    def get(self, todo_id):
        self.db.cursor.execute(
            "SELECT id, task_description,priority, completed FROM todos WHERE id = ?",
            (todo_id,),
        )
        return self.db.cursor.fetchone()

    def get_all(self):
        self.db.cursor.execute(
            "SELECT id, task_description, priority, completed FROM todos"
        )
        return self.db.cursor.fetchall()

    def update(self, todo_id, updated_data):
        update_query = "UPDATE todos SET {} WHERE id = ?".format(
            ", ".join(f"{key} = ?" for key in updated_data.keys())
        )
        values = list(updated_data.values())
        values.append(todo_id)
        self.db.cursor.execute(update_query, values)
        self.db.conn.commit()
        return self.db.cursor.rowcount > 0

    def delete(self, todo_id):
        self.db.cursor.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
        self.db.conn.commit()
        return self.db.cursor.rowcount > 0

    def mark_completed(self, todo_id):
        self.db.cursor.execute(
            "UPDATE todos SET completed = 1 WHERE id = ?", (todo_id,)
        )
        self.db.conn.commit()
        return self.db.cursor.rowcount > 0

    def mark_incomplete(self, todo_id):
        self.db.cursor.execute(
            "UPDATE todos SET completed = 0 WHERE id = ?", (todo_id,)
        )
        self.db.conn.commit()
        return self.db.cursor.rowcount > 0
