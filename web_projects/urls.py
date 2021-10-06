'''
Created on Oct 3, 2021

@author: cristian
'''
from django.urls import path
from . import views

app_name = "web_projects"

urlpatterns = [
    path("", views.web_projects, name="z"),
    ]