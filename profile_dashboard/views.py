from django.shortcuts import render
from .models import Profile
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    #update profile

    context = {}

    return render(request, "edit_profile.html", context)