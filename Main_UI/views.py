from django.shortcuts import render
from django.http import HttpResponse
from Main_UI.models import NetworkDatabase
from Main_UI.models import Settings
from django.shortcuts import redirect

# Create your views here.
def home(request):
    database = NetworkDatabase.objects.all()
    return render(request, 'Main_UI/home.html', locals())

def settings(request):
    email = Settings.objects.get(clef="email").valeur
    return render(request, 'Main_UI/settings.html', locals())

def about(request):
    return render(request, 'Main_UI/about.html', locals())

def delete_entry(request, ip_d, mac_d):
    element = NetworkDatabase.objects.get(ip=ip_d, mac=mac_d)
    element.delete()
    return redirect('home')
