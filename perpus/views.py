from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    nama_lokal = request.GET.get('nama')
    return render(request, 'perpus/index.tpl.html', {'nama': nama_lokal})


def home(request):
    return HttpResponse('ini default home!')
