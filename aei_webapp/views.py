from django.shortcuts import render

# Create your views here.
def home(request):
    '''
    Serves the home page.
    '''

    context = {}

    return render(request, 'home/home.html', context)
