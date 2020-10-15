from django.shortcuts import render

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        print('auth')
    else:
        print('not auth')
    return render(request, 'home.html', {})
