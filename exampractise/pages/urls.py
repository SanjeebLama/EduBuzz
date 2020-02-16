from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('courses', views.courses, name='courses'),
    path('about', views.about, name='about'),
    path('resources', views.resources, name='resources'),
    path('discussion', views.discussion, name='discussion'),

]
