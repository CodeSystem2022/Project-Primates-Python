from django.urls import path  # importamos el path para poder crear las rutas
from .views import listar_registros, crear_registros, eliminar_registros, editar_registros # importamos las funciones creadas en views- . -py
urlpatterns = [
    path('', listar_registros, name='registros'),
    path('crear/', crear_registros, name='crear_registros'),
    path('eliminar_registros/<int:registros_id>/', eliminar_registros, name='eliminar_registros'),
    path('editar_registros/<int:registros_id>/', editar_registros, name='editar_registros'),
]
#Aca se llaman las funciones creadas eSn views.py para ser mostradas en el navegador