from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('details/<int:task_id>/', views.Details, name='details'),  # Modified URL pattern
    path('details/', views.Details, name='details'),
    path('add_task/', views.add_task, name='add_task'),  # New URL pattern
    path('modify_task/', views.modify_task, name='modify_task'),
    path('delete_task/', views.delete_task, name='delete_task'),
]