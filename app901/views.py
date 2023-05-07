from multiprocessing import context
from pydoc import pager
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

projectList =[
    {
        'id':1,
        'titulo': 'home',
        'descripcion':'pagina de home',
    },
       {
        'id':2,
        'titulo': 'ventas',
        'descripcion':'pagina de ventas',
    },
       {
        'id':3,
        'titulo': 'envios',
        'descripcion':'pagina de envios',
    },
]
def mujer(request):
    projects = Project.objects.all()
    context={'projects': projects}
    return render(request, 'projects/mujer.html',context)

# def hombre(request):
#     projectObj = Project.objects.get()
#     return render(request, 'projects/hombre.html',{'project':projectObj})

def hombre(request):
    projects = Project.objects.all()
    context={'projects': projects}
    return render(request, 'projects/hombre.html',context)

def caballeros(request):
    projects = Project.objects.all()
    context={'projects': projects}
    return render(request, 'projects/caballeros.html',context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    print("projectObj:", projectObj)
    return render(request, 'projects/project.html', {'project': projectObj, 'tags':tags})
    
def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
       form = ProjectForm(request.POST,request.FILES)
    if form.is_valid():
            form.save()
            return redirect('home')
    context ={'form': form}
    return render(request, "projects/project_form.html",context)

def updateProject(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
       form = ProjectForm(request.POST,request.FILES, instance=project)
    if form.is_valid():
            form.save()
            return redirect('home')
    context ={'form': form}
    return render(request, "projects/project_form.html",context)

def deleteProject(request,pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('home')
    context = {'object': project}
    return render(request, 'projects/delete_object.html', context)