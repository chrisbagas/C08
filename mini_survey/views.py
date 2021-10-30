from django.shortcuts import redirect, render
from .forms import CreateSurveyForm
from .models import Survey


def index(request):
    survey_list = Survey.objects.all()
    context = {'survey_list': survey_list}
    return render(request, 'survey_main.html', context)


def details(request, survey_id):
    survey = Survey.objects.get(pk=survey_id)
    context = {'survey': survey}
    return render(request, context)


def vote(request, survey_id):
    survey = Survey.objects.get(pk=survey_id)

    if request.method == 'POST':
        selected_option = request.POST['survey']
        if selected_option == 'first_option':
            survey.first_option_count += 1
        elif selected_option == 'second_option':
            survey.second_option_count += 1
        elif selected_option == 'third_option':
            survey.third_option_count += 1

        survey.save()

        return redirect('detail', survey_id)

    context = {'survey': survey}
    return render(request, context)


def create(request):
    if request.method == 'POST':
        form = CreateSurveyForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('index')
    else:
        form = CreateSurveyForm()

    context = {'form': form}
    return render(request, 'survey_create.html', context)
