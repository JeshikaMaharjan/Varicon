# commented codes are by use of serializer


class TodoViewSet(viewsets.ViewSet):
    def list(self, request):
        todos = todo_repository.get_all()
        return render(request, "todo/todo_list.html", {"todos": todos})

        # todos = Todo.objects.all()
        # serializer = TodoSerializer(todos, many=True)
        # return Response(serializer.data)

    def create(self, request):
        if request.method == "POST":
            title = request.POST.get("title")
            description = request.POST.get("description")
            if title and description:
                todo = todo_repository.create(title, description)
                return JsonResponse({"id": todo.id}, status=201)
            return JsonResponse({"error": "Invalid request data"}, status=400)
        return JsonResponse({"error": "Invalid request method"}, status=405)

        # serializer = TodoSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
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

        # todo = Todo.objects.filter(pk=pk).first()
        # if not todo:
        #     return Response({'detail': 'To-Do not found'}, status=status.HTTP_404_NOT_FOUND)

        # serializer = TodoSerializer(todo, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        todo = todo_repository.get(todo_id)
        if not todo:
            return JsonResponse({"error": "To-Do not found"}, status=404)

        if request.method == "DELETE":
            todo_repository.delete(todo)
            return JsonResponse({"message": "To-Do deleted"}, status=200)
        return JsonResponse({"error": "Invalid request method"}, status=405)

        # todo = Todo.objects.filter(pk=pk).first()
        # if not todo:
        #     return Response({'detail': 'To-Do not found'}, status=status.HTTP_404_NOT_FOUND)

        # todo.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)

    def mark_done(self, request, pk=None):
        todo = todo_repository.get(todo_id)
        if not todo:
            return JsonResponse({"error": "To-Do not found"}, status=404)

        if request.method == "PUT":
            todo_repository.mark_completed(todo)
            return JsonResponse({"message": "To-Do marked as completed"}, status=200)
        return JsonResponse({"error": "Invalid request method"}, status=405)

        # todo = Todo.objects.filter(pk=pk).first()
        # if not todo:
        #     return Response({'detail': 'To-Do not found'}, status=status.HTTP_404_NOT_FOUND)

        # todo.completed = True
        # todo.save()
        # serializer = TodoSerializer(todo)
        # return Response(serializer.data)
