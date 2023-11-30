from django.shortcuts import render
from django.http import HttpResponse
from . models import Kegiatan
# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return HttpResponse('ini Halaman About')

def todos(request):
    items = Kegiatan.objects.all()
    return render(request,"kegiatan.html", {"todos":items})