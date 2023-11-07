class AddTodoCommand:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.completed = False


class EditTodoCommand:
    def __init__(self, task_id, new_description, priority):
        self.task_id = task_id
        self.new_description = new_description
        self.priority = priority


class DeleteTodoCommand:
    def __init__(self, task_id):
        self.task_id = task_id


class MarkAsDone:
    def __init__(self, task_id, completed):
        self.task_id = task_id
        self.completed = True
