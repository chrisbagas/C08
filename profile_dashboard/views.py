from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import Profile
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import base64
import json
from django.core.files.base import ContentFile
from django.contrib.auth.models import User

@login_required(login_url='/login/')
def profile(request):
    return render(request, 'profile.html')

@login_required(login_url='/login/')
def edit_profile(request):
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

@csrf_exempt
def get_profile_info_flutter(request, uname):
    user = User.objects.get(username = uname)
    profile = Profile.objects.get(user = user)

    data = serializers.serialize('json', [user, profile])
    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def edit_profile_flutter(request):
    response = {}
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        firstName = data['firstName']  
        lastName = data['lastName']  
        username = data['username']
        #email = data['email']
        bio = data['bio']
        file = data['file']
        nama = data['nama']
        image = ContentFile(base64.b64decode(file),nama)

        if firstName and lastName and username and bio and file and nama and image:
            profile = Profile.objects.get(user = User.objects.get(username = username))
            u_form = UserUpdateForm(request.POST or None, instance=profile.user)
            p_form = ProfileUpdateForm(request.POST or None,
                                        request.FILES or None,
                                        instance=profile)
            tmp_uform = u_form.save(commit = False)
            tmp_pform = p_form.save(commit = False)

            tmp_uform.firstName = firstName
            tmp_uform.lastName = lastName
            tmp_pform.bio = bio
            tmp_pform.image = image

            tmp_pform.save()
            tmp_uform.save()

            response = {
                'msg':  'Update profil Anda berhasil disimpan!',
                'id' : 1,
                'status': 'success'
            }

    return JsonResponse(response)

@csrf_exempt
def edit_profile_flutter_noPic(request):
    response = {}
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        firstName = data['firstName']  
        lastName = data['lastName']  
        username = data['username']
        bio = data['bio']

        if firstName and lastName and username and bio:
            profile = Profile.objects.get(user = User.objects.get(username = username))
            u_form = UserUpdateForm(request.POST or None, instance=profile.user)
            p_form = ProfileUpdateForm(request.POST or None,
                                        request.FILES or None,
                                        instance=profile)
            tmp_uform = u_form.save(commit = False)
            tmp_pform = p_form.save(commit = False)

            tmp_uform.firstName = firstName
            tmp_uform.lastName = lastName
            tmp_pform.bio = bio

            tmp_pform.save()
            tmp_uform.save()

            response = {
                'msg':  'Update profil Anda berhasil disimpan!',
                'id' : 1,
                'status': 'success'
            }

        return JsonResponse(response)
    else:
        return JsonResponse({"status": "error"})