from django.shortcuts import render, get_object_or_404
from .models import Event

def index(request):
    event=Event.objects.all()
    response = {'event':event}
    return render(request, 'index.html', response)

def event_detail(request,id):
    response={'event':get_object_or_404(Event,pk=id)}
    return render(request, 'event.html', response)