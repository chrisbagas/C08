from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from .models import Profile
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def edit_profile(request):
    # if request.method == 'POST':
    #     u_form = UserUpdateForm(request.POST, instance=request.user)
    #     p_form = ProfileUpdateForm(request.POST,
    #                                 request.FILES,
    #                                 instance=request.user.profile)
    #     if u_form.is_valid() and p_form.is_valid():
    #         u_form.save()
    #         p_form.save()
    #         return redirect('profile')
        # else:
        #         u_form = UserUpdateForm(instance=request.user)
        #         p_form = ProfileUpdateForm(instance=request.user.profile)

    u_form = UserUpdateForm(request.POST or None, instance=request.user)
    p_form = ProfileUpdateForm(request.POST or None,
                                        request.FILES or None,
                                        instance=request.user.profile)

    if request.is_ajax():
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return JsonResponse({
                'message': 'success'
        })

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'edit_profile.html', context)