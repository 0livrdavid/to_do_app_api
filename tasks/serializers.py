from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'deadline', 'priority', 
            'completed', 'created_at', 'updated_at', 'user', 'task_category'
        ]

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'title', 'description', 'deadline', 'priority', 
            'task_category'
        ]

class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'title', 'description', 'deadline', 'priority', 
            'completed', 'task_category'
        ]

class TaskDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id']
