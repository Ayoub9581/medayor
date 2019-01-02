from django.shortcuts import render,get_object_or_404,redirect



def view_404(request):
    return render(request,'medayor/error_pages/404.html',status=404)

def view_500(request):
    return render(request,'medayor/error_pages/505.html',status=500)
