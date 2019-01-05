from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .models import Project
from .forms import ProjectForm
from django.conf import settings
from django.contrib.auth import get_user_model
from accounts.models import Team

User = get_user_model()


def index(request):
    projects = Project.objects.all()
    teams = Team.objects.team()
    context = {
    'projects':projects,
    'teams':teams,
    }
    return render(request,'portfolio/home.html',context)

def launch(request):
    teams = Team.objects.team()
    context = {'teams':teams}
    if request.user.is_anonymous:
        return render(request,'portfolio/launch.html')
    else:
        return render(request,'portfolio/home.html',context)

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
