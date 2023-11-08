from domain.commands import (
    AddTodoCommand,
    EditTodoCommand,
    DeleteTodoCommand,
    MarkAsDone,
)
from domain.models import Task, TaskList


class ToDoCommandHandler:
    def __init__(self):
        self.task_id_counter = 0

    def handle(self, command):
        if isinstance(command, AddTodoCommand):
            self._create_task(command)
        elif isinstance(command, EditTodoCommand):
            self._edit_task(command)
        elif isinstance(command, MarkAsDone):
            self._mark_as_done_(command)
        elif isinstance(command, DeleteTodoCommand):
            self._delete_task(command)

    def _create_task(self, command):
        task = Task(self.task_id_counter, command.description, command.priority, False)
        TaskList(self.task_id_counter, "username", task)

    def _edit_task(self, command):
        task = Task.get(command.task_id)
        if task:
            Task(command.task_id, command.new_description, command.priority)

    def _mark_as_done_(self, command):
        task = TaskList.get(command.task_id)
        if task:
            Task["completed"] = True

    def _delete_task(self, command):
        if command.task_id in TaskList:
            TaskList.delete_task(command.task_id)
