# Entities
class User:
    def __init__(self, id: int, name: str, email: str, username: str, password: str):
        self.id = id
        self.name = name
        self.email = email
        self.username = username
        self.password = password


# Value objects
class Task:
    id: int
    task_description: str
    priority: int
    completed: bool


# Aggregates
class TaskList:
    def __init__(self, id: int, user: {User}, tasks: [Task]):
        self.tasks = {self.id: id, self.user: user, self.tasks: tasks}

    # def add_task(self, task: str, priority: int):
    #     # implementation incomplete

    def delete_task(self, task_id: int):
        if task_id in self.tasks:
            del self.tasks[task_id]

    # def edit_task(self, task_id: int, new_task: str, priority: int):
    #     pass
