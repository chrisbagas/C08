from django.urls import path
from .views import *

urlpatterns = [
    path('', lists, name='lists'),
    path('create/', create, name='create'),
    path('search/', search_results, name='search'),
    path('<int:survey_id>/', details, name='details'),
    path('<int:survey_id>/delete/', delete, name='delete'),
    path('<int:survey_id>/edit/', edit, name='edit'),
    path('<int:survey_id>/results/', results, name='results'),
    path('<int:survey_id>/vote/', vote, name='vote'),
    path('<int:survey_id>/edit/add/', add_option, name='add_option'),

    # Path for Flutter
    path('get-lists/', lists_json, name='get_lists'),
    path('create-from-flutter/', create_from_flutter, name='create_from_flutter'),
    path('<int:survey_id>/get-details/', details_json, name='get_details'),
    path('<int:survey_id>/get-options/', options_json, name='get_options'),
    path('<int:survey_id>/edit-from-flutter/', edit_from_flutter, name='edit_from_flutter'),
    path('<int:survey_id>/delete-from-flutter/', delete_from_flutter, name='delete_from_flutter'),
    path('<int:survey_id>/vote-from-flutter', vote_from_flutter, name='vote_from_flutter'),
    path('<int:survey_id>/edit-from-flutter/add/', add_option_from_flutter, name='add_option_from_flutter'),
]
