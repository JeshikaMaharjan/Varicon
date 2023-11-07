# Entities
class User:
    def __init__(self, id: int, name: str, email: str, username: str, password: str):
        self.id = id
        self.name = name
        self.email = email
        self.username = username
        self.password = password


# Value objects
class TaskItem:
    id: int
    name: str
    priority: int


# Aggregates
class Task:
    def __init__(self, id: int, user: {User}, tasks: [{TaskItem}]):
        self.id = id
        self.user = user
        self.tasks = tasks
        print("User", user)
        print(tasks)

    def add_task(task: str, priority: int):
        pass

    def delete_task(task_id: int):
        pass

    def edit_task(task_id: int, new_task: str, priority: int):
        pass


Task(1, {12, "Jeshika", "jeshika99@gmail.com", "jcka", "pass"}, [{1, "Do laundry", 3}])
# Task.add_task("Email", 2)
