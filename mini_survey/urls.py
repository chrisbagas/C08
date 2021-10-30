from django.urls import path
from .views import create, details, index, vote

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('<survey_id>/details/', details, name='details'),
    path('<survey_id>/vote/', vote, name='vote'),
]
