'''
Created on Sep 25, 2021

@author: cristian
'''
from django.urls import path
from . import views

appname = "front_page"
urlpatterns = [
    path("", views.front_page, name="front_page"),
    ]