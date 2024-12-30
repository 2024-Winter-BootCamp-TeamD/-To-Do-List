from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)  # 제목
    completed = models.BooleanField(default=False)  # 완료
    important = models.BooleanField(default=False)  # 중요

    def __str__(self):
        return self.title
