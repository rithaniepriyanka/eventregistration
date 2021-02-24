from django.shortcuts import render
from .models import Participants
from django.core.exceptions import ValidationError

# Create your views here.
def home(request):
    context = {}
    return render(request, "eventapplication/home.html" , context)

def registration(request):
    context = {}
    if request.method == "POST":
        p1 = Participants()
        p1.username = request.POST.get('username','-')
        p1.email = request.POST.get('email','-')
        p1.phone = request.POST.get('phone','000')
        p1.instituition = request.POST.get('instituition','-')

        if len(Participants.objects.all()) > 26:
            return render(request,'eventapplication/error.html' ,conntext)

        else:
            p1.save()
            return render(request, 'eventapplication/success.html' ,context)

    if request.method == 'GET':
        context['username'] = ''
        context['email'] = ''
        context['phone'] = ''
        context['institution'] = ''

        
    return render(request, "eventapplication/registration.html" , context)

def listofparticipants(request):
    context = {}
 
    context['participants'] = Participants.objects.all()
    
    return render(request, "eventapplication/listofparticipants.html" , context)

def eventAdmin(request):
    context={}
    result=Participants.objects.all()
    context['answers']=result
    return render(request,'event/eventAdmin.html', context)