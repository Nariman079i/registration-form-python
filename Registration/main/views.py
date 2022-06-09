from django.shortcuts import render , redirect
from django.views.generic import ListView
from .models import *
from .forms import *


class Objects(ListView):
    model = Person
    context_object_name = 'user_data'
    template_name = 'main/users.html'
    extra_context = {'title':'Данные пользователя'}
def main(requests):

    if requests.method == "POST":
        form = RegForm(requests.POST)

        if form.is_valid():
            try:
                Person.objects.create(**form.cleaned_data)
                return redirect('main')
            except:
                form.add_error(None , 'erroe')
    else:
        form = RegForm()
    return render(requests ,'main/main.html' , context={'form' :form})
