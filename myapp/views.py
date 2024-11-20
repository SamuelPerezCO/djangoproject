from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):
    return HttpResponse("Index page")

def hello(request, username):
    print(username)
    return HttpResponse("<h1>Hello %s</h1>" % username)

def about(request):
    return HttpResponse('<h2>About</h2>')

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects , safe=False)

def tasks(request, id):
    task = get_object_or_404(Task,id = id)
    return HttpResponse('task: %s' % task.title)