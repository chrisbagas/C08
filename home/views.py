from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import FeedbackForm
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