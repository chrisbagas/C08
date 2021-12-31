from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import base64
import json
from django.core.files.base import ContentFile
from .models import Event
from .forms import EventForm

def index(request):
    event=Event.objects.all().order_by('-created')
    response = {'event':event}
    return render(request, 'event.html', response)

def event_detail(request,id):
    response={'event':get_object_or_404(Event,pk=id)}
    return render(request, 'detail.html', response)

@login_required(login_url="/admin/login")
def event_form(request):
    form = EventForm(request.POST or None, request.FILES or None)
    data = {}
    if request.is_ajax():
        if form.is_valid():
            form.save()
            data['Nama'] = form.cleaned_data.get('Nama')
            data['status'] = 'ok'
            return JsonResponse(data)
            
    response = {
        'form': form,
    }
    return render(request,'Event_Form.html', response) #Return NoteForm ke dalam bentuk html

@csrf_exempt
def jsonget(request):
    posts = Event.objects.all()
    response = serializers.serialize('json', posts)
    return HttpResponse(response, content_type = 'application/json')

@csrf_exempt
def add(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data['title']
        tanggal = data['tanggal']
        waktu = data['waktu']
        media = data['media']
        tipe = data['tipe']
        Url = data['url']
        deskripsi = data['deskripsi']
        file1 = data['file1']
        name1 = data['name1']
        image1 = ContentFile(base64.b64decode(file1),name1)
        file2 = data['file2']
        name2 = data['name2']
        image2 = ContentFile(base64.b64decode(file2),name2)
        eventform = Event(Nama=title, Tanggal=tanggal, Waktu = waktu, Media = media, Tipe = tipe, url = Url, Deskripsi = deskripsi, Card_Image = image1, Page_Image = image2)
        eventform.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)