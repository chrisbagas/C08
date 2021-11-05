from django.contrib import admin
from mini_survey.models import Option, Survey, Vote


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ['title', 'creator', 'pub_date']
    search_fields = ['title', 'creator__username']
    date_hierarchy = 'pub_date'


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ['survey', 'text']
    search_fields = ['text', 'survey__title']
    autocomplete_fields = ['survey']


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['survey', 'option', 'user']
    search_fields = ['survey__title', 'option__text', 'user__username']
    autocomplete_fields = ['survey', 'option', 'user']
