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
    return render(request, 'index.html')  # 메인 HTML 템플릿 렌더링

# 작업 조회 및 생성
@swagger_auto_schema(
    method='get',
    responses={200: TaskSerializer(many=True)},  # GET 응답
    operation_description="작업을 조회합니다."
)
@swagger_auto_schema(
    method='post',
    request_body=TaskSerializer,  # POST 요청 데이터
    responses={201: TaskSerializer},
    operation_description="작업을 생성합니다."
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

# 작업 생성
@swagger_auto_schema(
    method='post',
    request_body=TaskSerializer,
    responses={201: TaskSerializer},
    operation_description="작업을 생성합니다."
)
@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 작업 수정
@swagger_auto_schema(
    method='patch',
    request_body=TaskSerializer,
    responses={200: TaskSerializer},
    operation_description="작업을 수정합니다."
)
@api_view(['PATCH'])
def update_task(request, id):
    try:
        task = Task.objects.get(pk=id)
    except Task.DoesNotExist:
        return Response({'error': 'Task를 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = TaskSerializer(task, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 작업 상태 토글
@swagger_auto_schema(
    method='patch',
    responses={200: TaskSerializer},
    operation_description="작업의 상태를 변경합니다."
)
@api_view(['PATCH'])
def toggle_task_status(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({'error': 'Task를 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

    task.completed = not task.completed
    task.save()
    serializer = TaskSerializer(task)
    return Response(serializer.data)

# 작업 삭제
@swagger_auto_schema(
    method='delete',
    responses={204: openapi.Response(description="Task가 삭제되었습니다.")},
    operation_description="작업을 삭제합니다."
)
@api_view(['DELETE'])
def delete_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({'error': 'Task를 찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)

    task.delete()
    return Response({'message': 'Task가 삭제되었습니다.'}, status=status.HTTP_204_NO_CONTENT)

# 선택 작업 삭제
@swagger_auto_schema(
    method='delete',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'ids': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_INTEGER))
        },
        required=['ids']
    ),
    responses={204: openapi.Response(description="선택된 작업들이 삭제되었습니다.")},
    operation_description="선택된 작업들을 삭제합니다."
)
@api_view(['DELETE'])
def delete_selected_tasks(request):
    ids = request.data.get('ids', [])
    Task.objects.filter(id__in=ids).delete()
    return Response({'message': '선택된 작업들이 삭제되었습니다.'}, status=status.HTTP_204_NO_CONTENT)
