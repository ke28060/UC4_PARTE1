from django.shortcuts import render, HttpResponse,redirect


# Create your views here.
def index(request):
    return render(request,'index.html')


def Cursos(request):
    return render(request,'Index.html')

def Crearcursos(request):
    return render(request,'Crearcursos.html')
def carreras(request):
    return render(request,'carreras.html')
def Crearcarreras(request):
    return render(request,'crearcarreras.html')
