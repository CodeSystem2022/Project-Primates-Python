from django.shortcuts import render, redirect
from .models import Registro
from .forms import RegistroForm
# Create your views here.
#EN ESTE ARCHIVO SE CREAN LAS VISTAS DE LA APLICACION EN ESTE CASO "REGISTROS" CON HTML
def listar_registros(request):
    registro = Registro.objects.all() # con esto le decimos que nos traiga todos los registros de la base de datos y rempleza a "SELECT * FROM registros_registro"
    return render(request, 'listar_registros.html',{'registros': registro})
def crear_registros(request):
    registro = Registro(nombre=request.POST['Registro'], descripcion=request.POST['descripcion'])
    registro.save() #aca le decimos que guarde el registro creado anteriormente en la base de datos
    return redirect('registros') #aca le decimos que nos redireccione a la pagina principal "registros"

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
