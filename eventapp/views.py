from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from .forms import Detailform
# Create your views here.
def index(request):
    events = Event.objects.all()
    context={
        'events' : events #value 'event' refers to the variable event=event.object.....
    }
    return render(request,'eventapp/index.html', context)

def eventdetail(request,pk):
    event_s = Event.objects.get(pk=pk)
    if request.method=='POST':
        form=Detailform(request.POST)
        if form.is_valid():
            applicant=form.save(commit=False)
            #commit=false: don't commit to database(as we have to add event also)
            applicant.event=event_s
            applicant.save()
    form = Detailform()
    context={
        'event' : event_s, #value 'event' refers to the variable event=event.object.....
        'form' : form
    }
    return render(request,'eventapp/detail.html', context)

def login(request):
    return render(request,'eventapp/login.html')