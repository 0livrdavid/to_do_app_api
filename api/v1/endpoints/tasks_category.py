from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from tasks_category.models import TaskCategory
from tasks_category.serializers import TaskCategorySerializer, TaskCategoryCreateSerializer, TaskCategoryUpdateSerializer, TaskCategoryDeleteSerializer
from rest_framework import status

@permission_classes([IsAuthenticated])
def list_task_categories(request):
    categories = TaskCategory.objects.filter(user=request.user)
    serializer = TaskCategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@permission_classes([IsAuthenticated])
def create_task_category(request):
    serializer = TaskCategoryCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAuthenticated])
def update_task_category(request, category_id):
    try:
        category = TaskCategory.objects.get(id=category_id, user=request.user)
    except TaskCategory.DoesNotExist:
        return Response({'error': 'Task category not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = TaskCategoryUpdateSerializer(category, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAuthenticated])
def delete_task_category(request, category_id):
    try:
        category = TaskCategory.objects.get(id=category_id, user=request.user)
        serializer = TaskCategoryDeleteSerializer(category)
        if serializer.is_valid():
            category.delete()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except TaskCategory.DoesNotExist:
        return Response({'error': 'Task category not found'}, status=status.HTTP_404_NOT_FOUND)