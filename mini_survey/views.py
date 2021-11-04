from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import AddOptionForm, CreateSurveyForm, EditSurveyForm
from .models import Option, Survey, Vote


def lists(request):
    survey_list = Survey.objects.all()
    survey_count = survey_list.count()
    # Make pagination to show 10 survey per page
    paginator = Paginator(survey_list, 10)
    page_num = request.GET.get('page')
    surveys = paginator.get_page(page_num)
    context = {
        'surveys': survey_list,
        'survey_count': survey_count
    }
    return render(request, 'survey/survey_lists.html', context)


def details(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    option_count = survey.option_set.count()
    context = {
        'survey': survey,
        'option_count': range(0, option_count)
    }
    return render(request, 'survey/survey_details.html', context)


def results(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    context = {
        'survey': survey
    }
    return render(request, 'survey/survey_results.html', context)


@login_required(login_url='/signup/login')
def create(request):
    if request.method == 'POST':
        form = CreateSurveyForm(request.POST)
        if form.is_valid:
            survey = form.save(commit=False)
            survey.creator = request.user
            survey.save()
            new_option1 = Option(
                survey=survey, text=form.cleaned_data['option1']).save()
            new_option2 = Option(
                survey=survey, text=form.cleaned_data['option2']).save()

            return redirect('/survey')
    else:
        form = CreateSurveyForm()

    context = {
        'form': form,
    }
    return render(request, 'survey/survey_create.html', context)


@login_required(login_url='/signup/login')
def edit(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    if request.user != survey.creator:
        return redirect('/survey')

    if request.method == 'POST':
        form = EditSurveyForm(request.POST, instance=survey)
        if form.is_valid:
            form.save()
            return redirect('/survey')
    else:
        form = EditSurveyForm(instance=survey)

    context = {
        'form': form,
        'survey': survey,
    }
    return render(request, 'survey/survey_edit.html', context)


@login_required(login_url='/signup/login')
def delete(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    if request.user != survey.creator:
        redirect('/survey')

    survey.delete()
    return redirect('/survey')


@login_required(login_url='/signup/login')
def add_option(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    if request.user != survey.creator:
        return redirect('\survey')

    if request.method == 'POST':
        form = AddOptionForm(request.POST)
        if form.is_valid:
            new_option = form.save(commit=False)
            new_option.survey = survey
            new_option.save()
            return redirect()
    else:
        form = AddOptionForm()

    context = {
        'form': form,
    }
    return render(request, 'survey/add_option.html', context)


@login_required(login_url='/signup/login')
def vote(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    option_id = request.POST.get('option')
    if not survey.vote_requirement(request.user):
        messages.error(request, "You already voted for this survey!")
        return redirect('/survey')

    if option_id:
        option = Option.objects.get(pk=option_id)
        vote = Vote(user=request.user, survey=survey, option=option)
        vote.save()
    else:
        messages.error(request, "No option selected!")
        return redirect('detail', survey_id)

    context = {
        'survey': survey,
    }
    return render(request, 'survey/survey_result.html', context)
