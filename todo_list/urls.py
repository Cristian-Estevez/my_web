'''
Created on Oct 4, 2021

@author: cristian
'''
from django.urls import path
from . import views

app_name = "todo_list"

urlpatterns = [
    path("", views.ToDoListView.as_view(), name='todo_list'),
    path("task_confirm_delete/<int:pk>/", views.TaskDeleteView.as_view(), name="task_delete_view"),
    path("task_add_new_task/", views.TaskCreateView.as_view(), name="add_task"),
    ]