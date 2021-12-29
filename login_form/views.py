from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout as django_logout
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import CreateUser
from django.contrib.auth.backends import UserModel

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

@login_required
def logout(request):
    django_logout(request)
    return redirect('login')


@csrf_exempt
def loginWithFlutter(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return JsonResponse({
                "status": True,
                "username": request.user.username,
                "message": "Successfully Logged In!"
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Failed to Login, Account Disabled."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Failed to Login, check your email/password."
        }, status=401)


@csrf_exempt
def signupWithFlutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        username = data["username"]
        email = data["email"]
        password1 = data["password1"]

        newUser = UserModel.objects.create_user(
            username=username,
            email=email,
            password=password1,
        )

        newUser.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)


@csrf_exempt
def logoutFlutter(request):
    try:
        logout(request)
        return JsonResponse({
            "status": True,
            "message": "Successfully Logged out!"
        }, status=200)
    except:
        return JsonResponse({
            "status": False,
            "message": "Failed to Logout"
        }, status=401)
