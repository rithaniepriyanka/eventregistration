from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, "eventapplication/home.html" , context)

def registration(request):
    context = {}
    return render(request, "eventapplication/registration.html" , context)

def listofparticipants(request):
    context = {}
    return render(request, "eventapplication/listofparticipants.html" , context)