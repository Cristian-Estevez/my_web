'''
Created on Oct 4, 2021

@author: cristian
'''
from django import forms
from django.forms import ModelForm
from .models import ToDoList 

class ToDoListForm(ModelForm):
    completed = forms.BooleanField(widget=forms.CheckboxInput(),required=False, label="completed")
    
    class Meta:
        model = ToDoList
        fields = '__all__'