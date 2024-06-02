from rest_framework import serializers
from .models import TaskCategory

class TaskCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskCategory
        fields = ['id', 'name', 'description', 'user']

class TaskCategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskCategory
        fields = ['name', 'description']

class TaskCategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskCategory
        fields = ['name', 'description']

class TaskCategoryDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskCategory
        fields = ['id']