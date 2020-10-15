from django.urls import path
from phonebook import views

urlpatterns = [
    path('', views.home, name='nome'),
]