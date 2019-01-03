from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .models import Project
from .forms import ProjectForm
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()




def index(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request,'portfolio/index.html',context)

def launch(request):
    if request.user.is_anonymous:
        return render(request,'portfolio/launch.html')
    else:
        return render(request,'portfolio/index.html')

def projects(request):
    # projects = Project.objects.all()
    # nomdomain = projects.first()
    # context = {'projects':projects, 'nomdomain':nomdomain.domaine_project.nom_domaine,}
    return render(request,'portfolio/projects.html')

def create_project(request):
    form = ProjectForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.medayor_user = request.user
            instance.save()
            return redirect('services')
        else:
            form = ProjectForm()
    context = { 'form':form , 'domainname':form.domaine_project}
    return render(request,'portfolio/createproject.html',context)
