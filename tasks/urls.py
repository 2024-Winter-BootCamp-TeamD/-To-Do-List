from django.urls import path
from . import views

urlpatterns = [
    # 메인 페이지
    path('', views.index, name='index'),

    # 작업 목록 조회 및 작업 생성
    path('tasks/', views.task_list, name='task_list'),  # GET: 조회, POST: 생성

    # 작업 생성 (명확히 분리된 URL 사용 가능)
    path('tasks/create/', views.create_task, name='create_task'),

    # 작업 수정
    path('tasks/<int:id>/update/', views.update_task, name='update_task'),  # PATCH: 특정 작업 수정

    # 작업 상태 토글
    path('tasks/<int:pk>/toggle/', views.toggle_task_status, name='toggle_task_status'),  # PATCH: 완료 상태 변경

    # 작업 삭제
    path('tasks/<int:pk>/delete/', views.delete_task, name='delete_task'),  # DELETE: 특정 작업 삭제

    # 선택 작업 삭제
    path('tasks/delete-selected/', views.delete_selected_tasks, name='delete_selected_tasks'),  # DELETE: 여러 작업 삭제
]
