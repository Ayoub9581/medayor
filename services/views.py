from django.shortcuts import render,get_object_or_404,redirect
from .models import Service
from .forms import ServiceForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def services_home(request):
    services = Service.objects.all()
    context = {
        'services':services,
    }
    return render(request,'services/services.html',context)

@login_required(login_url='/accounts/login')
def add_service(request):
    form = ServiceForm(request.POST or None , request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            # isinstance.description_service = request.POST['definition_service'].startwith(instance.definition_service)
            instance.medayor_user = request.user
            instance.save()
            print('Service created !!!!')
        return redirect('services')
    context = {
            'form':form,
        }

    return render(request,'services/create_service.html',context)

def service_detail(request,slug):
    instance = get_object_or_404(Service,slug=slug)
    context = {
        'instance':instance
    }
    return render(request,'services/servicedetail.html',context)

@login_required(login_url='/accounts/login')
def edit_service(request,slug=None):
    instance = get_object_or_404(Service, slug=slug)
    if not request.user.is_admin:
        raise Http404
    form = ServiceForm(request.POST or None , request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect(instance.get_absolute_url())
    context = {
        'form':form,
        'instance':instance.nom_service
    }

    return render(request,'services/create_service.html',context)
