from django.urls import path
from . import views
from users.views import (
    register_user, delete_user, login_user, list_users
)
from tasks.views import (
    list_tasks, create_task, update_task, 
    delete_task, update_task_completed
)

urlpatterns = [
    path("user/register/", register_user, name="register"),
    path("user/delete/<int:user_id>", delete_user, name="delete_user"),
    path("user/login/", login_user, name="login"),
    path("user/list/", list_users, name="list_users"),
    
    path("task/list/", list_tasks, name="list_tasks"),
    path("task/create/", create_task, name="create_task"),
    path("task/update/<int:task_id>/", update_task, name="update_task"),
    path("task/delete/<int:task_id>/", delete_task, name="delete_task"),
    path("task/update_completed/<int:task_id>/", update_task_completed, name="update_task_completed"),
    
    path("category/list/", views.list_categories, name="list_categories"),
    path("category/create/", views.create_category, name="create_category"),
    path("category/update/<int:category_id>/", views.update_category, name="update_category"),
    path("category/delete/<int:category_id>/", views.delete_category, name="delete_category"),
]