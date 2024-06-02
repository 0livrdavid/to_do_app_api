from django.db import models
from users.models import User
from tasks_category.models import TaskCategory

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    deadline = models.DateTimeField(blank=True, null=True)
    PRIORITY_CHOICES = [
        ('low', 'Baixa'),
        ('medium', 'Média'),
        ('high', 'Alta'),
    ]
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='low')
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task_category = models.ForeignKey(TaskCategory, on_delete=models.CASCADE)