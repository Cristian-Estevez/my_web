'''
Created on Sep 26, 2021

@author: cristian
'''
from django.urls import path
from . import views

app_name = "about_me"
urlpatterns = [
    path("", views.about_me, name = "about_me"),
    ]