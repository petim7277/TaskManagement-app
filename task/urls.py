from django.urls import path
from . import views

request_mapping = [
    path('task/', views.create_task)

]
