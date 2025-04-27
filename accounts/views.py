from django.shortcuts import render
from accounts.forms import *


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            
    form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context=context)
