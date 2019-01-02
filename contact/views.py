from django.shortcuts import render,redirect
from .forms import ContactForm
# Create your views here.


def send_contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.adresse_ip = request.META['REMOTE_ADDR']
            instance.host_contact =  request.META['HTTP_HOST']
            instance.server_name_contact =  request.META['SERVER_NAME']
            instance.http_user_agent =  request.META['HTTP_USER_AGENT']
            instance.save()
        return redirect('home')
    context = {'form':form,}
    return render(request,'contact/contact.html',context)
