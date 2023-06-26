from django.forms import ModelForm
from .models import Registro #Importamos el modelo  de la clase Registro

class RegistroForm(ModelForm): #aqui se crea la nueva clase RegistroForm
    class Meta:
        model = Registro
        fields = '__all__'