from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import render

# index 뷰
def index(request):
    return render(request, 'index.html')  # index
# 작업 조회, 생성
@swagger_auto_schema(
    method='get',
    responses={200: TaskSerializer(many=True)},  # GET
    operation_description="Get all tasks"
)
@swagger_auto_schema(
    method='post',
    request_body=TaskSerializer,  # POST
    responses={201: TaskSerializer},
    operation_description="Create a new task"
)
@api_view(['GET', 'POST'])
def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all().order_by('-important', 'completed', '-id')
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 토글
@swagger_auto_schema(
    method='patch',
    responses={200: TaskSerializer},
    operation_description="Toggle task completion status"
)
@api_view(['PATCH'])
def toggle_task_status(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    task.completed = not task.completed
    task.save()
    serializer = TaskSerializer(task)
    return Response(serializer.data)

# 작업 삭제
@swagger_auto_schema(
    method='delete',
    responses={204: openapi.Response(description="Task deleted")},
    operation_description="Delete a task"
)
@api_view(['DELETE'])
def delete_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    task.delete()
    return Response({'message': 'Task deleted'}, status=status.HTTP_204_NO_CONTENT)
