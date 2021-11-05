from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime, date
from .models import BlogPost
from .forms import BlogPostForm
from django.urls import reverse_lazy

def index(request):
    posts = BlogPost.objects.all()
    response = {'posts': posts}
    return render(request, 'blog/index.html', response)

def post(request, slug):
    post = BlogPost.objects.get(slug=slug)
    response = {'post': post}
    return render(request, 'blog/post.html', response)

@login_required(login_url='/login/')
def add_post(request):
    form = BlogPostForm(request.POST, request.FILES)
    if request.method == 'POST' and form.is_valid:
        temp = form.save(commit=False)
        temp.author = request.user
        temp.save()
        return HttpResponseRedirect('/blog')
    context = {
        'form': form
    }
    return render(request, 'blog/add_post.html', context)

@login_required(login_url='/login/')
def edit_post(request, slug):
    postedit = BlogPost.objects.get(slug=slug)
    form = BlogPostForm(request.POST, request.FILES, instance=postedit)
    if request.method == 'POST' and form.is_valid:
        temp = form.save(commit=False)
        temp.author = request.user
        temp.save()
        return HttpResponseRedirect('/blog')
    context = {
        'form': form,
        'post': post
    }
    return render(request, 'blog/edit_post.html', context)

@login_required(login_url='/login/')
def delete_post(request, slug):
    post = BlogPost.objects.get(slug=slug)
    if request.method == 'POST':
        post.delete()
        return HttpResponse(200);
        #return HttpResponseRedirect('/blog')
    context = {
    }
    #success_url = reverse_lazy('blog/')
    return render(request, 'blog/delete_post.html', context)
