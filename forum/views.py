from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Forum

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def homeView(request):
    hashtag = request.GET.get("hashtag", "")
    if hashtag:
        return HttpResponseRedirect(reverse("home") + "#{0}".format(hashtag))
    context = {'forums': Forum.objects.all()}
    return render(request, 'home.html', context)

def detailView(request, pk):
    context = {'forum': Forum.objects.get(pk=pk)}
    return render(request, 'forum_detail.html', context)