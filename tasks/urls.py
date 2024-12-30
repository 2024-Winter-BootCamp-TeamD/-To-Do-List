from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # 템플릿
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/<int:pk>/toggle/', views.toggle_task_status, name='toggle_task_status'),
    path('tasks/<int:pk>/delete/', views.delete_task, name='delete_task'),
]
