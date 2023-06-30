from django.shortcuts import render, redirect
from .models import Registro
from .forms import RegistroForm
# EN ESTE ARCHIVO SE CREAN LAS VISTAS DE LA APLICACIÓN EN ESTE CASO "REGISTROS" CON HTML
# ACÁ SE CREAN LAS FUNCIONES QUE SE LLAMAN EN EL ARCHIVO urls.py


def portada_index(request):
    return render(request, 'portada_index.html')


def listar_registros(request):
    registro = Registro.objects.all()
    return render(request, 'listar_registros.html', {'registros': registro})
# Con esto le decimos que nos traiga todos los registros de la base de datos y remplaza a
# "SELECT * FROM registros_registro"


def crear_registros(request):
    registro = Registro(nombre=request.POST['nombre'], descripcion=request.POST['descripcion'])
    registro.save()  # Acá le decimos que guarde el registro creado anteriormente en la base de datos
    return redirect('registros')  # Acá le decimos que nos redireccione a la página principal "registros"


def eliminar_registros(request, registros_id):
    eliminar_registros = Registro.objects.get(id=registros_id)
    eliminar_registros.delete()
    return redirect('registros')


def editar_registros(resquest, registros_id):
    registro = Registro.objects.get(id=registros_id)
    forms = RegistroForm(resquest.POST or None, instance=registro)
    if forms.is_valid() and resquest.POST:
        forms.save()
        return redirect('registros')
    return render(resquest, "editar_diagnostico.html", {'forms': forms})
