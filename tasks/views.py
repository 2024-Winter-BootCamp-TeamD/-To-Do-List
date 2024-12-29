from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    if request.method == "POST":
        if "task" in request.POST:  # 할 일 추가
            task_title = request.POST.get("task")
            if task_title:
                important = "*" in task_title  # 입력에 '*' 기호 확인
                Task.objects.create(
                    title=task_title.replace("*", "").strip(),  # '*' 제거 후 저장
                    important=important
                )
        elif "complete" in request.POST:  # 상태 변경
            task_id = request.POST.get("complete")
            task = Task.objects.get(id=task_id)
            task.completed = not task.completed
            task.save()
        elif "delete" in request.POST:  # 할 일 삭제
            task_id = request.POST.get("delete")
            task = get_object_or_404(Task, id=task_id)
            task.delete()
        return redirect("task_list")

    # 중요 항목을 우선적으로 정렬
    incomplete_tasks = Task.objects.filter(completed=False).order_by('-important', 'id')
    completed_tasks = Task.objects.filter(completed=True).order_by('-important', 'id')
    return render(request, "todolist.html", {
        "incomplete_tasks": incomplete_tasks,
        "completed_tasks": completed_tasks
    })
