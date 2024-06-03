from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from tasks_category.models import TaskCategory
from tasks_category.serializers import TaskCategorySerializer, TaskCategoryCreateSerializer, TaskCategoryUpdateSerializer
from rest_framework import status

@permission_classes([IsAuthenticated])
def task_category_list_task_category(request):
    try:
        categories = TaskCategory.objects.filter(user=request.user)
        if categories.exists():
            serializer = TaskCategorySerializer(categories, many=True)
            return Response({'success': True, 'data': serializer.data, 'msg': 'Categorias recuperadas com sucesso'}, status=status.HTTP_200_OK)
        else:
            return Response({'success': False, 'data': None, 'msg': 'Nenhuma categoria encontrada'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'success': False, 'data': None, 'msg': 'Erro interno do servidor: ' + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@permission_classes([AllowAny])
def task_category_list_all_task_category(request):
    try:
        categories = TaskCategory.objects.all()
        if categories.exists():
            serializer = TaskCategorySerializer(categories, many=True)
            return Response({'success': True, 'data': serializer.data, 'msg': 'Todas as categorias recuperadas com sucesso'}, status=status.HTTP_200_OK)
        else:
            return Response({'success': False, 'data': None, 'msg': 'Nenhuma categoria encontrada'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'success': False, 'data': None, 'msg': 'Erro interno do servidor: ' + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@permission_classes([IsAuthenticated])
def task_category_create_task_category(request):
    try:
        serializer = TaskCategoryCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'success': True, 'data': serializer.data, 'msg': 'Categoria criada com sucesso'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'success': False, 'data': serializer.errors, 'msg': 'Erros de validação'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'success': False, 'data': None, 'msg': 'Erro interno do servidor: ' + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@permission_classes([IsAuthenticated])
def task_category_update_task_category(request, task_category_id):
    try:
        task_category = TaskCategory.objects.get(id=task_category_id, user=request.user)
        serializer = TaskCategoryUpdateSerializer(task_category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'data': serializer.data, 'msg': 'Categoria atualizada com sucesso'}, status=status.HTTP_200_OK)
        else:
            return Response({'success': False, 'data': None, 'msg': 'Erros de validação: ' + str(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)
    except TaskCategory.DoesNotExist:
        return Response({'success': False, 'data': None, 'msg': 'Categoria de tarefa não encontrada'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'success': False, 'data': None, 'msg': 'Internal Server Error: ' + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@permission_classes([IsAuthenticated])
def task_category_delete_task_category(request, task_category_id):
    try:
        category = TaskCategory.objects.get(id=task_category_id, user=request.user)
        category.delete()
        return Response({'success': True, 'data': None, 'msg': 'Categoria excluída com sucesso'}, status=status.HTTP_200_OK)
    except TaskCategory.DoesNotExist:
        return Response({'success': False, 'data': None, 'msg': 'Categoria de tarefa não encontrada'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'success': False, 'data': None, 'msg': 'Erro interno do servidor: ' + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
