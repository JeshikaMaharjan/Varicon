from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import ToDoRepositoryImpl

todo_repository = ToDoRepositoryImpl()


def todo_list(request):
    todos = todo_repository.get_all()
    return render(request, "todo/todo_list.html", {"todos": todos})


def todo_detail(request, todo_id):
    todo = todo_repository.get(todo_id)
    if todo:
        return render(request, "todo/todo_detail.html", {"todo": todo})
    return JsonResponse({"error": "To-Do not found"}, status=404)


def create_todo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        if title and description:
            todo = todo_repository.create(title, description)
            return JsonResponse({"id": todo.id}, status=201)
        return JsonResponse({"error": "Invalid request data"}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)


def update_todo(request, todo_id):
    todo = todo_repository.get(todo_id)
    if not todo:
        return JsonResponse({"error": "To-Do not found"}, status=404)

    if request.method == "PUT":
        title = request.POST.get("title")
        description = request.POST.get("description")
        if title and description:
            todo = todo_repository.update(todo, title, description)
            return JsonResponse({"message": "To-Do updated"}, status=200)
        return JsonResponse({"error": "Invalid request data"}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)


def delete_todo(request, todo_id):
    todo = todo_repository.get(todo_id)
    if not todo:
        return JsonResponse({"error": "To-Do not found"}, status=404)

    if request.method == "DELETE":
        todo_repository.delete(todo)
        return JsonResponse({"message": "To-Do deleted"}, status=200)
    return JsonResponse({"error": "Invalid request method"}, status=405)


def mark_done(request, todo_id):
    todo = todo_repository.get(todo_id)
    if not todo:
        return JsonResponse({"error": "To-Do not found"}, status=404)

    if request.method == "PUT":
        todo_repository.mark_completed(todo)
        return JsonResponse({"message": "To-Do marked as completed"}, status=200)
    return JsonResponse({"error": "Invalid request method"}, status=405)
