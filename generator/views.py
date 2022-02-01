from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,"generator/home.html")

def password(request):
    thepassword = ''
    characters = list('qwertyuiopasdfghjklzxcvbnm')
    lenght = int(request.GET.get('length',12))
    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('specialcharacters'):
        characters.extend(list('!@#$%^&*()!?><'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    for x in range(lenght):
        thepassword += random.choice(characters)

    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    return render(request, "generator/password.html", {'password': thepassword})

def reviu(request):
    return render(request,"generator/reviu.html")