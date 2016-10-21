from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'base.html', {})


def form_new(request):
    form = PostForm()
    return render(request, 'form/form_new.html', {'form': form})


def form_list(request):
    """form = PostForm()
    return render(request, 'form/form_new.html', {'form': form})
    """
