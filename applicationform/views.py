# -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from forms import PostForm
from django.core.mail import send_mail, BadHeaderError


def index(request):
    return render(request, 'base.html', {})


def form_new(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():

            subject = "Inscription " # form.cleaned_data['subject']
            from_email = form.cleaned_data['email']

            message = ""

            for field in form:
                message += '<p><strong>'+str(field.label)+'</strong>:'+str(field.value())+'</p>'

            
            try:
                send_mail(subject, message, from_email, ['rlefranc@lefresnoy.net'])

            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return HttpResponse("OK")




            #return redirect('applicationform.views.post_send_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'form/form_new.html', {'form': form})



def form_list(request):
    """form = PostForm()
    return render(request, 'form/form_new.html', {'form': form})
    """
