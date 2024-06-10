from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from api.v1.endpoints.users import (
    users_register_user, users_login_user, users_list_users, users_delete_user, users_logout_user
)

@api_view(['GET'])
@permission_classes([AllowAny])
def list_users(request):
    response = users_list_users(request)
    return Response({
        "success": response.data['success'],
        "data": response.data['data'],
        "msg": response.data['msg']
    }, status=response.status_code)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    response = users_register_user(request)
    return Response({
        "success": response.data['success'],
        "data": response.data['data'],
        "msg": response.data['msg']
    }, status=response.status_code)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    response = users_login_user(request)
    return Response({
        "success": response.data['success'],
        "data": response.data['data'],
        "msg": response.data['msg']
    }, status=response.status_code)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    response = users_logout_user(request)
    return Response({
        "success": response.data['success'],
        "data": response.data['data'],
        "msg": response.data['msg']
    }, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_user(request, user_id):
    response = users_delete_user(request, user_id)
    return Response({
        "success": response.data['success'],
        "data": response.data['data'],
        "msg": response.data['msg']
    }, status=response.status_code)
