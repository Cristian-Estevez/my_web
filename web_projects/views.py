from django.shortcuts import render

# Create your views here.
def web_projects(request):
    return render(request, "web_projects/web_projects.html")