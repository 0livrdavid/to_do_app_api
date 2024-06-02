from rest_framework.decorators import api_view

# USERS ENDPOINTS
from .endpoints.users import users_register_user, users_login_user, users_list_users, users_delete_user

@api_view(['POST'])
def register_user(request):
    return users_register_user(request)

@api_view(['DELETE'])
def delete_user(request, user_id):
    return users_delete_user(request, user_id)

@api_view(['POST'])
def login_user(request):
    return users_login_user(request)

@api_view(['GET'])
def list_users(request):
    return users_list_users(request)



# TASKS ENDPOINTS
from .endpoints.tasks import tasks_list_tasks, tasks_create_task, tasks_update_task, tasks_delete_task, tasks_update_completed

@api_view(['GET'])
def list_tasks(request):
    return tasks_list_tasks(request)

@api_view(['POST'])
def create_task(request):
    return tasks_create_task(request)

@api_view(['PUT', 'PATCH'])
def update_task(request, task_id):
    return tasks_update_task(request, task_id)

@api_view(['DELETE'])
def delete_task(request, task_id):
    return tasks_delete_task(request, task_id)

@api_view(['PATCH'])
def update_task_completed(request, task_id):
    return tasks_update_completed(request, task_id)


# TASKS CATEGORY ENDPOINTS
from .endpoints.tasks_category import list_task_categories, create_task_category, update_task_category, delete_task_category

@api_view(['GET'])
def list_categories(request):
    return list_task_categories(request)

@api_view(['POST'])
def create_category(request):
    return create_task_category(request)

@api_view(['PUT', 'PATCH'])
def update_category(request, category_id):
    return update_task_category(request, category_id)

@api_view(['DELETE'])
def delete_category(request, category_id):
    return delete_task_category(request, category_id)
