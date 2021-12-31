from django.shortcuts import redirect, render
from django.http.response import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

from .forms import FeedbackForm
from .models import FeedbackModel


def index(request):
    return render(request, 'index.html')


@login_required(login_url='login')
def feedback(request):
    feedback_form = FeedbackForm(request.POST or None)

    if request.method == 'POST':
        if feedback_form.is_valid():
            feedback_form.save()

            return redirect('homepage')

    context = {
        'feedback_form': feedback_form
    }

    return render(request, 'feedback.html', context)


@csrf_exempt
def json(request):
    posts = FeedbackModel.objects.all()
    response = serializers.serialize('json', posts)
    return HttpResponse(response, content_type='application/json')


@csrf_exempt
def add(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data['message']
        rating = data['rating']
        feedbackF = FeedbackModel(message=message, rating=rating)
        feedbackF.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
