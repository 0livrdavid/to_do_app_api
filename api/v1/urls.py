from django.urls import path
from users.views import (
    register_user, delete_user, login_user, list_users, logout_user
)
from tasks.views import (
    list_tasks, create_task, update_task, 
    delete_task, update_task_completed, list_all_tasks
)
from tasks_category.views import (
    list_task_category, create_task_category, update_task_category, delete_task_category, list_all_task_category
)

urlpatterns = [
    path("user/list/", list_users, name="list_users"),
    path("user/signup/", register_user, name="register"),
    path("user/signin/", login_user, name="login"),
    path("user/signout/", logout_user, name="logout"),
    path("user/delete/<int:user_id>/", delete_user, name="delete_user"),
    
    path("task/list/<int:task_id>/", list_tasks, name="list_tasks"),
    path("task/list_all/", list_all_tasks, name="list_all_tasks"),
    path("task/create/", create_task, name="create_task"),
    path("task/update/<int:task_id>/", update_task, name="update_task"),
    path("task/delete/<int:task_id>/", delete_task, name="delete_task"),
    path("task/update_completed/<int:task_id>/", update_task_completed, name="update_task_completed"),
    
    path("task_category/list/", list_task_category, name="list_task_category"),
    path("task_category/list_all/", list_all_task_category, name="list_all_task_category"),
    path("task_category/create/", create_task_category, name="create_task_category"),
    path("task_category/update/<int:task_category_id>/", update_task_category, name="update_task_category"),
    path("task_category/delete/<int:task_category_id>/", delete_task_category, name="delete_task_category"),
]

