from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect('/contacts')
    else:
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

def delete(request, id):
    if request.method == 'POST':
        Contact.objects.get(id=id).delete()
        return redirect('/contacts')

def create(request):
    if request.method == 'POST':
        contact = Contact(
            first_name = request.POST['first_name'],
            second_name = request.POST['second_name'],
            email = request.POST['email'],
            phone_number = request.POST['phone_number'],
            user = request.user
        )
        contact.save()
        return redirect('/contacts')

def edit(request, id):
    if request.method == 'POST':
        c = Contact.objects.get(id=id)
        c.first_name = request.POST['first_name']
        c.second_name = request.POST['second_name']
        c.email = request.POST['email']
        c.phone_number = request.POST['phone_number']
        c.save()
        return redirect('/contacts')
        


