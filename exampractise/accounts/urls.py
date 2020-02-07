from django.urls import path
from . import views

urlpatterns = [
    path('test', views.test, name='test'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('insideAuth', views.insideAuth, name='insideAuth'),

]