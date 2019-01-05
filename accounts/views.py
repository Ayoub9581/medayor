from django.shortcuts import render, redirect
from .forms import UserCreationForm, UserLoginForm
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth import login, get_user_model, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from .models import MyUser

User = get_user_model()

def register_user(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        print('user_created')
        return redirect('home')
    return render(request, 'accounts/register.html',{'form':form})

def user_login(request, *args, **kwargs):
    form  = UserLoginForm(request.POST or None)
    if form.is_valid():
        user_obj = form.cleaned_data.get('user_obj')
        login(request,user_obj)
        messages.success(request,'you have succufully logged')
        return redirect('home')
    return render(request, 'accounts/login.html', {'form':form})


def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/accounts/login')
def get_profile(request,id):
    currentuser = get_object_or_404(MyUser, id=id)
    posts = Post.objects.filter(publisher__exact=request.user)
    total_post_per_user = posts.count()
    if currentuser.id is not request.user.id:
         # messages.warning(request, 't a pas lautorisation.')
         # redirect('home')
         raise Http404

    context = {
        'currentuser':currentuser,
        'totalpost':total_post_per_user,
        'posts':posts,
    }
    return render(request, 'accounts/profile.html',context)
