from database import Database


class TodoRepository:
    def __init__(self, database_name):
        self.db = Database(database_name)


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
