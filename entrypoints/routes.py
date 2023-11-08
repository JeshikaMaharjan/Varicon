# Endpoints
from . import views
import path

urlpatterns = [
    path("", views.todo_list, name="todo_list"),
    path("<int:todo_id>/", views.todo_detail, name="todo_detail"),
    path("create/", views.create_todo, name="create_todo"),
    path("update/<int:todo_id>/", views.update_todo, name="update_todo"),
    path("delete/<int:todo_id>/", views.delete_todo, name="delete_todo"),
    path("complete/<int:todo_id>/", views.mark_done, name="mark_completed"),
]
