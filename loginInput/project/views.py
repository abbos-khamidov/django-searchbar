from django.shortcuts import render
from . models import AddPostForm


def index(request):
    return render(request, 'index.html')

def login(request):
    form = AddPostForm()
    
    data = {
        'form': form,
    }
    
    return render(request, 'login.html', data)