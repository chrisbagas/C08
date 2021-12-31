from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from .forms import AddOptionForm, CreateSurveyForm, EditSurveyForm
from .models import Option, Survey, Vote
import json


def lists(request):
    survey_list = Survey.objects.all()
    survey_count = survey_list.count()
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


@login_required(login_url='/login')
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


@login_required(login_url='/login')
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


@login_required(login_url='/login')
def delete(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    if request.user != survey.creator:
        redirect('/survey')

    survey.delete()
    return redirect('/survey')


@login_required(login_url='/login')
def add_option(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    if request.user != survey.creator:
        return redirect('/survey')

    if request.method == 'POST':
        form = AddOptionForm(request.POST)
        if form.is_valid:
            new_option = form.save(commit=False)
            new_option.survey = survey
            new_option.save()
            return redirect('edit', survey_id)
    else:
        form = AddOptionForm()

    context = {
        'form': form,
        'survey': survey,
    }
    return render(request, 'survey/add_option.html', context)


@login_required(login_url='/login')
def vote(request, survey_id):
    survey = get_object_or_404(Survey, pk=survey_id)
    option_id = request.POST.get('option')
    if not survey.vote_requirement(request.user):
        return redirect('/survey')

    if option_id:
        option = Option.objects.get(pk=option_id)
        vote = Vote(user=request.user, survey=survey, option=option)
        vote.save()
    else:
        return redirect('detail', survey_id)

    context = {
        'survey': survey,
    }
    return render(request, 'survey/survey_results.html', context)


def search_results(request):
    if request.is_ajax():
        res = None
        survey = request.POST.get('survey')
        qs = Survey.objects.filter(title__icontains=survey)
        if len(qs) > 0 and len(survey) > 0:
            data = []
            for pos in qs:
                item = {
                    'pk': pos.pk,
                    'title': pos.title,
                    'creator': pos.creator
                }
                data.append(item)
            res = data
        else:
            res = 'No survey found'

        return JsonResponse({'data': res})
    return JsonResponse({})


def lists_json(request):
    survey_list = Survey.objects.all()
    for survey in survey_list:
        survey.creator_username = survey.creator.username
    lists = serializers.serialize('json', survey_list)
    return HttpResponse(lists, content_type='application/json')

def details_json(request, survey_id):
    survey = Survey.objects.get(pk=survey_id)
    ls = []
    dc = {}

    dc['title'] = survey.title
    dc['description'] = survey.description
    dc['creator'] = survey.creator.username
    dc['survey_count'] = survey.get_survey_count()

    ls.append(dc)
    details = json.dumps(ls)

    return HttpResponse(details, content_type='application/json')

def options_json(request, survey_id):
    survey = Survey.objects.get(pk=survey_id)
    ls = []

    for option in survey.option_set.all():
        ls.append({'option' : option.text, 'option_count' : option.get_option_count()})

    options = json.dumps(ls)
    
    return HttpResponse(options, content_type='application/json')


@csrf_exempt
def create_from_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data['title']
        description = data['description']

        survey = Survey(
            title = title,
            description = description,
            creator = request.user,
        )
        survey.save()

        return JsonResponse({'status': 'success'}, status=200)

    return JsonResponse({'status': 'error'}, status=401)

@csrf_exempt
def edit_from_flutter(request, survey_id):
    if request.method == 'POST':
        survey = Survey.objects.get(pk=survey_id)

        title = json.loads(request.body)['title']
        description = json.loads(request.body)['description']

        survey.title = title
        survey.description = description

        survey.save()

        return JsonResponse({'status': 'success'}, status=200)

    return JsonResponse({'status': 'error'}, status=401)

@csrf_exempt
def delete_from_flutter(request, survey_id):
    survey = Survey.objects.get(pk=survey_id)
    survey.delete()
    return HttpResponse("")

@csrf_exempt
def add_option_from_flutter(request, survey_id):
    if request.method == 'POST':
        survey = Survey.objects.get(pk=survey_id)
        text = json.loads(request.body)['text']
        
        option = Option(
            survey = survey,
            text = text,
        )
        option.save()

        return JsonResponse({'status': 'success'}, status=200)

    return JsonResponse({'status': 'error'}, status=401)

@csrf_exempt
def vote_from_flutter(request, survey_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_vote = data['vote']

        return JsonResponse({'status': 'success'}, status=200)

    return JsonResponse({'status': 'error'}, status=401)