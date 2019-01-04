from django.shortcuts import render,redirect
from .forms import ContactForm
from django.contrib import messages
# Create your views here.




def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def send_contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.adresse_ip = get_client_ip(request)
            instance.http_user_agent =  request.META.get('HTTP_USER_AGENT')
            instance.save()
            messages.success(request,'<b>{}</b> merci de nous envoyer un message '.format(instance.name))
        return redirect('home')
    else:
        form = ContactForm()
    context = {'form':form,}
    return render(request,'contact/contact.html',context)
