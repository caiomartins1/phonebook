from django.urls import path
from phonebook import views

urlpatterns = [
    path('', views.home, name='nome'),
    path('contacts/', views.contacts, name='contacts'),
    path('contacts/delete/<int:id>/', views.delete, name='delete'),
    path('contacts/create', views.create, name='create'),
    path('contacts/edit/<int:id>/', views.edit, name='edit')
]