from django.shortcuts import render, redirect
from .models import proovedores
# Create your views here.


def inicio_vista(request):
    laslistas=proovedores.objects.all()
    return render(request,"gestionarMateria.html",{"mislistas":laslistas})


def registrarproo(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    telefono=request.POST["numtelefono"]
    edad=request.POST["numedad"]
    ine=request.POST["numine"]
    permiso=request.POST["textpermiso"]
    matricula=request.POST["textmatricula"]

    guardarmateria=proovedores.objects.create(codigo=codigo, nombre=nombre, telefono=telefono, edad=edad, ine=ine, permiso=permiso, matricula=matricula)

    return redirect("/")

def seleccionarproo(request,codigo):
    materia=proovedores.objects.get(codigo=codigo)
    return render(request,"editarmateria.html",{"mismaterias":materia})