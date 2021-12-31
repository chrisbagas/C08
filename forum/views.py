from datetime import datetime
from django.contrib.auth import models
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import request
from django.http.response import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.generic import View
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Comment, Forum
import json


from django.contrib.humanize.templatetags.humanize import naturaltime
from django.utils.text import Truncator

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def homeView(request):
    hashtag = request.GET.get("hashtag", "")
    if hashtag:
        return HttpResponseRedirect(reverse("home") + "#{0}".format(hashtag))
    context = {'forums': Forum.objects.all()}
    return render(request, 'home.html', context)

@csrf_exempt
class createForum(View):
    def get(self, request):
        authorr = request.user
        titlee = request.GET.get('title', None)
        bodyy = request.GET.get('body', None)
        # time_created = models.DateTimeField(auto_now_add=True),
        obj = Forum.objects.create(
            author = authorr,
            title = titlee,
            body = bodyy,
            # time_created = time_created,
            # time_modified = time_created,
        )
        
        forum = {
            'pk': obj.pk,
            'author': obj.author.username,
            'title': Truncator(obj.title).words(20),
            'body': obj.body,
            'time_modified': naturaltime(obj.time_modified),
        }
        data = {
            'forum': forum,
        }

        return JsonResponse(data)


    

@csrf_exempt
class createComment(View):
    def get(self, request):
        forumm = request.GET.get('forum', None)
        authorr = request.user
        bodyy = request.GET.get('body', None)
        # time_created = models.DateTimeField(auto_now_add=True),
        obj = Comment.objects.create(
            forum = forumm,
            author = authorr,
            body = bodyy,
        )
        
        comment = {
            'pk': obj.pk,
            'author': obj.author.username,
            'title': obj.titlee,
            'body': obj.body,
            'time_modified': naturaltime(obj.time_modified),
        }
        data = {
            'comment': comment,
        }
        return JsonResponse(data)


@csrf_exempt
class deleteForum(View):
    def get(self, request):
        pk = request.GET.get('pk', None)
        Forum.objects.get(pk=pk).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@csrf_exempt
@login_required(login_url='/login/')
def delete_forum(request, pk):
    forum = Forum.objects.get(pk=pk)
    print(pk)
    if (request.method == 'POST'):
        forum.delete()
        return HttpResponse(200);
    return redirect('/forum')

def detailView(request, pk):
    context = {
        'forum': Forum.objects.get(pk=pk),
        }
    return render(request, 'forum_detail.html', context)

@csrf_exempt
def get_json(request):
    forums = Forum.objects.all().order_by("-time_modified")
    for a in forums:
        a.author_username = a.author.username
    response = serializers.serialize('json', forums)
    return HttpResponse(response, content_type = 'application/json')


@csrf_exempt
def create_forum_flutter(request):
    if request.method == "POST":
        data = json.loads(request.body)
        title = data['title']
        body = data['body']
        forum = Forum(
            title=title,
            body=body,
            author=request.user,
        )
        forum.save()
        return JsonResponse({"status": "success"})
    else:
        return JsonResponse({"status": "error"})
