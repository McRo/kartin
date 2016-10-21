from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    #return render(request, 'applicationform/templates/base.html', {})
     html = "<html><body>It is now </body></html>"
     return HttpResponse(html)


def form_new(request):
    form = PostForm()
    return render(request, 'form/form_new.html', {'form': form})
