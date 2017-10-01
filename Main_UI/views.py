from django.shortcuts import render
from django.http import HttpResponse
from Main_UI.models import NetworkDatabase

# Create your views here.
def home(request):
    database = NetworkDatabase.objects.all()
    return render(request, 'Main_UI/home.html', locals())

def settings(request):
    modele = ["ip","a","b"]
    return render(request, 'Main_UI/settings.html')
