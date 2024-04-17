from django.urls import path
from . import views

urlpatterns = [
    path('find/', views.task_list),
    path('write/<int:id>/', views.task_detail, name='find_task_byId'),
    path('create/', views.create_user),
    path('getUser/', views.get_all_users),
    path('deleteUser/<int:id>/', views.delete_user, name='delete_user'),
    path('update/<int:id>/', views.update_user, name='update_user')

]
