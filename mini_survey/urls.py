from django.urls import path
from .views import *

urlpatterns = [
    path('', lists, name='lists'),
    path('create/', create, name='create'),
    path('search/', search_results, name='search'),
    path('<int:survey_id>/', details, name='details'),
    path('<int:survey_id>/delete/', delete, name='delete'),
    path('<int:survey_id>/edit/', edit, name='edit'),
    path('<int:survey_id>/results', results, name='results'),
    path('<int:survey_id>/vote/', vote, name='vote'),
    path('<int:survey_id>/edit/add', add_option, name='add_option')
]
