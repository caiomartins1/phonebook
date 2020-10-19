from django.urls import path
from phonebook import views

urlpatterns = [
    path('', views.home, name='nome'),
    path('contacts/', views.contacts, name='contacts')
]