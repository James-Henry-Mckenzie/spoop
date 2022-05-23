from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .forms import CreateForm

# Create your views here.


def button(request):
    return render(request, 'home.html')


def output(request):
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    math = datetime.now()
    math = int(math.strftime("%S"))
    math += 1
    program = 1
    return render(request, 'home.html', {'data':current_time, 'stuff':math, 'program':program})

def poop(request):
    return render(request, 'poop.html')


def create(request):
    form = CreateForm(request.POST)
    name = ''  
    number_3 = 0
    number_2 = 0
    number_1 = 0

    if form.is_valid():
        name = form.cleaned_data.get("name")
        check = form.cleaned_data.get("check")
        number_1 = form.cleaned_data.get("nu")
        number_2 = form.cleaned_data.get("nu_2")
        number_3 = number_1 + number_2

    return render(request, 'create.html', {'form':form, 'name':name, 'number_3':number_3, 'number_1':number_1, 'number_2':number_2})


