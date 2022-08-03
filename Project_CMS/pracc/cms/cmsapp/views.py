
# importing models and libraries
from django import forms
from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import UsersForm
from django.contrib.auth.models import User, auth


# from .models import User
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

class UserListView(ListView):
    model = User
    template_name = 'index.html'



class SiteIndexView(CreateView):
    model = User
    fields = ['status']
    success_url = reverse_lazy('index')
    template_name = 'site/index.html'

 
def register(request):
    if request.method == 'POST':
        first_name = request.POST['regfname']
        last_name = request.POST['reglname']
        email = request.POST['regemail']
        username = request.POST['regusername']
        password = request.POST['regpass']
        confirm_password = request.POST['regrepass']
        if password == confirm_password:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'Username is taken')
                return redirect('cmsapp:register')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'Email is taken')
                return redirect('cmsapp:register')
            else:
                user = User.objects.create_user(username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name)
                user.save()
                return redirect('cmsapp:login_user')
        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect('cmsapp:register')
    else:
        return render(request, 'signup.html')
def login_user(request):
    if request.method == 'POST':
        username = request.POST['logusername']
        password = request.POST['logpass']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('cmsapp:index')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('cmsapp:login_user')
    else:
        return render(request, 'login.html')