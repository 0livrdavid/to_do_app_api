from rest_framework.response import Response

from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from users.models import User
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from users.serializers import UserSerializer, UserRegisterSerializer, UserLoginSerializer, UserDeleteSerializer

@permission_classes([AllowAny])
def users_register_user(request):
    try:
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            if instance:
                return Response({'success': True, 'data': None, 'msg': 'Usuário criado com sucesso'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'success': False, 'data': None, 'msg': 'Instância de usuário inválida'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'success': False, 'data': None, 'msg': 'Falha na validação'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'success': False, 'data': None, 'msg': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@permission_classes([AllowAny])
def users_delete_user(request, user_id):
    try:
        serializer = UserDeleteSerializer(data={'id': user_id})
        if serializer.is_valid():
            instance = serializer.delete(serializer.validated_data)
            if instance:
                return Response({'success': True, 'data': None, 'msg': 'Usuário deletado com sucesso'}, status=status.HTTP_200_OK)
            else:
                return Response({'success': False, 'data': None, 'msg': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'success': False, 'data': None, 'msg': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'success': False, 'data': None, 'msg': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@permission_classes([AllowAny])
def users_login_user(request):
    try:
        serializer = UserLoginSerializer(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
            print(user)
            if user:
                print('entrou')
                try:
                    print(user)
                    if not User.objects.filter(pk=user.pk).exists():
                        return Response({'success': False, 'data': None, 'msg': 'Usuário não existe no banco de dados'}, status=status.HTTP_404_NOT_FOUND)
                    token, _ = Token.objects.get_or_create(user=user)
                    print(token.key)
                    return Response({'success': True, 'data': {'token': token.key}, 'msg': 'Login bem-sucedido'}, status=status.HTTP_200_OK)
                except Exception as e:
                    print("erro 2", e)
                    return Response({'success': False, 'data': None, 'msg': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response({'success': False, 'data': None, 'msg': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'success': False, 'data': None, 'msg': 'Nome de usuário e senha são necessários'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print("erro 1", e)
        return Response({'success': False, 'data': None, 'msg': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@permission_classes([AllowAny])
def users_list_users(request):
    try:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        if serializer:
            return Response({'success': True, 'data': serializer.data, 'msg': 'Usuários listados com sucesso'}, status=status.HTTP_200_OK)
        else:
            return Response({'success': False, 'data': None, 'msg': 'Serializador inválido'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'success': False, 'data': None, 'msg': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)