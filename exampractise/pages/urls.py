from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('browse', views.browse, name='browse'),
    path('contacts', views.contacts, name='contacts'),
    path('subject/<subject>', views.subject, name='subject'),
    path('subject/<subject>/quiz', views.quiz, name='quiz'),

]
