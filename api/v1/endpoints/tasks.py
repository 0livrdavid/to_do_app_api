from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from tasks.models import Task
from tasks.serializers import (
    TaskSerializer, TaskCreateSerializer, TaskUpdateSerializer
)

@permission_classes([IsAuthenticated])
def tasks_list_tasks(request):
    try:
        if request.user.is_authenticated:
            tasks = Task.objects.filter(user=request.user)
            if tasks.exists():
                serializer = TaskSerializer(tasks, many=True)
                return Response({'success': True, 'data': serializer.data, 'msg': 'Tarefas recuperadas com sucesso'}, status=status.HTTP_200_OK)
            else:
                return Response({'success': False, 'data': None, 'msg': 'Nenhuma tarefa encontrada'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'success': False, 'data': None, 'msg': 'Usuário não autenticado'}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response({'success': False, 'data': None, 'msg': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@permission_classes([IsAuthenticated])
def tasks_list_all_tasks(request):
    try:
        tasks = Task.objects.all()
        if tasks.exists():
            serializer = TaskSerializer(tasks, many=True)
            return Response({'success': True, 'data': serializer.data, 'msg': 'Todas as tarefas recuperadas com sucesso'}, status=status.HTTP_200_OK)
        else:
            return Response({'success': False, 'data': None, 'msg': 'Nenhuma tarefa encontrada'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'success': False, 'data': None, 'msg': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@permission_classes([IsAuthenticated])
def tasks_create_task(request):
    try:
        if request.user.is_authenticated:
            serializer = TaskCreateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response({'success': True, 'data': serializer.data, 'msg': 'Tarefa criada com sucesso'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'success': False, 'data': None, 'msg': 'Erro de validação'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'success': False, 'data': None, 'msg': 'Usuário não autenticado'}, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response({'success': False, 'data': None, 'msg': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@permission_classes([IsAuthenticated])
def tasks_update_task(request, task_id):
    try:
        if request.user.is_authenticated:
            task = Task.objects.get(id=task_id, user=request.user)
            serializer = TaskUpdateSerializer(task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'success': True, 'data': serializer.data, 'msg': 'Tarefa atualizada com sucesso'}, status=status.HTTP_200_OK)
            else:
                return Response({'success': False, 'data': None, 'msg': 'Erro de validação'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'success': False, 'data': None, 'msg': 'Usuário não autenticado'}, status=status.HTTP_401_UNAUTHORIZED)
    except Task.DoesNotExist:
        return Response({'success': False, 'data': None, 'msg': 'Tarefa não encontrada'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'success': False, 'data': None, 'msg': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@permission_classes([IsAuthenticated])
def tasks_delete_task(request, task_id):
    try:
        if request.user.is_authenticated:
            task = Task.objects.get(id=task_id, user=request.user)
            task.delete()
            return Response({'success': True, 'data': None, 'msg': 'Tarefa deletada com sucesso'}, status=status.HTTP_200_OK)
        else:
            return Response({'success': False, 'data': None, 'msg': 'Usuário não autenticado'}, status=status.HTTP_401_UNAUTHORIZED)
    except Task.DoesNotExist:
        return Response({'success': False, 'data': None, 'msg': 'Tarefa não encontrada'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'success': False, 'data': None, 'msg': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@permission_classes([IsAuthenticated])
def tasks_update_completed(request, task_id):
    try:
        if request.user.is_authenticated:
            task = Task.objects.get(id=task_id, user=request.user)
            completed_status = request.data.get('completed')
            if completed_status is not None:
                task.completed = completed_status
                task.save()
                serializer = TaskSerializer(task)
                return Response({'success': True, 'data': serializer.data, 'msg': 'Tarefa atualizada com sucesso'}, status=status.HTTP_200_OK)
            else:
                return Response({'success': False, 'data': None, 'msg': 'Atualização de status de conclusão não fornecida'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'success': False, 'data': None, 'msg': 'Usuário não autenticado'}, status=status.HTTP_401_UNAUTHORIZED)
    except Task.DoesNotExist:
        return Response({'success': False, 'data': None, 'msg': 'Tarefa não encontrada'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'success': False, 'data': None, 'msg': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)