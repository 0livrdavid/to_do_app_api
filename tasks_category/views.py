from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from api.v1.endpoints.tasks_category import (
    task_category_list_task_category, task_category_create_task_category,
    task_category_update_task_category, task_category_delete_task_category,
    task_category_list_all_task_category
)
from rest_framework.permissions import IsAuthenticated, AllowAny

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_task_category(request):
    response = task_category_list_task_category(request)
    return Response({
        "success": response.data['success'],
        "data": response.data['data'],
        "msg": response.data['msg']
    }, status=response.status_code)
    
@api_view(['GET'])
@permission_classes([AllowAny])
def list_all_task_category(request):
    response = task_category_list_all_task_category(request)
    return Response({
        "success": response.data['success'],
        "data": response.data['data'],
        "msg": response.data['msg']
    }, status=response.status_code)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_task_category(request):
    response = task_category_create_task_category(request)
    return Response({
        "success": response.data['success'],
        "data": response.data['data'],
        "msg": response.data['msg']
    }, status=response.status_code)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_task_category(request, task_category_id):
    response = task_category_update_task_category(request, task_category_id)
    return Response({
        "success": response.data['success'],
        "data": response.data['data'],
        "msg": response.data['msg']
    }, status=response.status_code)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_task_category(request, task_category_id):
    response = task_category_delete_task_category(request, task_category_id)
    return Response({
        "success": response.data['success'],
        "data": response.data['data'],
        "msg": response.data['msg']
    }, status=response.status_code)