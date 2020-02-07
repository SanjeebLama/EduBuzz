from django.urls import path
from . import views

urlpatterns = [
    # path('',views.vuetify,name='vuetify'),
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    # path("pdf/example", views.print_pdf, name="print_pdf")
    # path('search',views.search,name='search'),
]
