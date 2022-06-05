from django.shortcuts import render , redirect
from .models import *
from .forms import *

def main(requests):

    if requests.method == "POST":
        form = RegForm(requests.POST)
        if form.is_valid():
            try:
                Person.objects.create(**form.cleaned_data)
                redirect('main')
            except:
                form.add_error(None , "Error")
    else:
        form = RegForm()
    return render(requests ,'main/main.html' , context={'form' :form} )