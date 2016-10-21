from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^form/new/$', views.form_new, name='form_new'),
]
