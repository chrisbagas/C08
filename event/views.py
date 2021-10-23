from django.shortcuts import render
from .models import Event

def index(request):
    event=Event.object.all()
    response = {'event':event}
    return render(request, 'index.html', response)

def event_detail(request,id):
    event=Event.object.get(id=id)
    response={'event':event}
    return render(request, 'event.html', response)