from django.contrib.auth import models
from django.http.response import HttpResponseRedirect, JsonResponse
from django.views.generic import View
from django.shortcuts import render
from django.urls import reverse
from .models import Comment, Forum


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

class createComment(View):
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
            'title': obj.titlee,
            'body': obj.body,
            'time_modified': naturaltime(obj.time_modified),
        }
        data = {
            'forum': forum,
        }
        return JsonResponse(data)

class deleteForum(View):
    def  get(self, request):
        pk = request.GET.get('pk', None)
        Forum.objects.get(pk=pk).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

def detailView(request, pk):
    context = {
        'forum': Forum.objects.get(pk=pk),
        }
    return render(request, 'forum_detail.html', context)