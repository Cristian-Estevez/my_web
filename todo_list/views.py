from django.views.generic import ListView, View
from .models import ToDoList
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from .forms import ToDoListForm
from django.contrib import messages


class ToDoListView(ListView):
    context_object_name = 'todo_list'
    template_name = "todo_list/todo_list.html"
    queryset = ToDoList.objects.all()
    
class TaskCreateView(View):
    template = "todo_list/todo_list_form.html"
    success_url = reverse_lazy("todo_list:todo_list")
    
    def get(self, request):
        task_form = ToDoListForm()
        return render(request, self.template, {"form": task_form})
    
    def post(self, request):
        if request.method == "POST":
            task_form = ToDoListForm(request.POST)
            
            if task_form.is_valid():
                task_form = task_form.save()
                messages.success(request, "Task added successfully")
            else:
                return redirect("todo_list:todo_list")
        return redirect(self.success_url)
    
    
class TaskDeleteView(View):
    model = ToDoList
    template = "todo_list/task_delete_view.html"
    success_url = reverse_lazy("todo_list:todo_list")
    
    def get(self, request, pk):
        task = get_object_or_404(self.model, pk=pk)
        return render(request, self.template, {"task": task})
    
    def post(self, request, pk):
        task = get_object_or_404(self.model, pk=pk)
        task.delete()
        return redirect(self.success_url)
