from django.shortcuts import render,redirect
from .forms import ContactForm
from django.contrib import messages
# Create your views here.


def send_contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.adresse_ip = request.META.get('REMOTE_ADDR',None)
            instance.http_user_agent =  request.META.get('HTTP_USER_AGENT')
            instance.save()
            messages.success(request,'merci de nous envoyer un message {}'.format(instance.name))
        return redirect('home')
    else:
        form = ContactForm()
    context = {'form':form,}
    return render(request,'contact/contact.html',context)
