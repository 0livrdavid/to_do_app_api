from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from api.v1.endpoints.tasks import (
    tasks_list_tasks, tasks_create_task, tasks_update_task, 
    tasks_delete_task, tasks_update_completed, tasks_list_all_tasks
)
from rest_framework.permissions import IsAuthenticated, AllowAny

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_tasks(request, task_id):
    response = tasks_list_tasks(request, task_id)
    return Response({
        "success": response.data['success'],
        "data": response.data['data'],
        "msg": response.data['msg']
    }, status=response.status_code)
    
@api_view(['GET'])
@permission_classes([AllowAny])
def list_all_tasks(request):
    response = tasks_list_all_tasks(request)
    return Response({
        "success": response.data['success'],
        "data": response.data['data'],
        "msg": response.data['msg']
    }, status=response.status_code)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_task(request):
    response = tasks_create_task(request)
    return Response({
        "success": response.data['success'],
        "data": response.data['data'],
        "msg": response.data['msg']
    }, status=response.status_code)

@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def update_task(request, task_id):
    response = tasks_update_task(request, task_id)
    return Response({
        "success": response.data['success'],
        "data": response.data['data'],
        "msg": response.data['msg']
    }, status=response.status_code)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_task(request, task_id):
    response = tasks_delete_task(request, task_id)
    return Response({
        "success": response.data['success'],
        "data": response.data['data'],
        "msg": response.data['msg']
    }, status=response.status_code)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_task_completed(request, task_id):
    response = tasks_update_completed(request, task_id)
    return Response({
        "success": response.data['success'],
        "data": response.data['data'],
        "msg": response.data['msg']
    }, status=response.status_code)