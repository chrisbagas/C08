from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import CreateUser

# Create your views here.

def signupPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUser()
        if request.method == 'POST':
            form = CreateUser(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Akun telah dibuat dengan username ' + user + ". Silakan login.")
                return redirect('login')
        context = {'form': form}
        return render(request, 'signup.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user )
                return redirect('index')
            else:
                messages.info(request, 'username atau password salah. ')
        context = {}
        return render(request, 'login.html', context)

def logout(request):
    logout(request)
    return redirect('login')
