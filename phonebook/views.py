from django.shortcuts import render
from .models import Contact

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def contacts(request):
    if request.user.is_authenticated:
        contacts = request.user.contact_set.all()
        context = {
            'contacts': contacts
        }
        return render(request, 'contacts.html', context)
    else: 
        return render(request, 'error.html', {})

