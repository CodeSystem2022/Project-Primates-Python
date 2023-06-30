from django.urls import path  # importamos el path para poder crear las rutas
# Importamos las funciones creadas en views- . -py
from .views import portada_index, listar_registros, crear_registros, eliminar_registros, editar_registros

urlpatterns = [
    path('', portada_index, name='portada_index'),
    path('registros', listar_registros, name='registros'),
    path('crear/', crear_registros, name='crear_registros'),
    path('eliminar_registros/<int:registros_id>/', eliminar_registros, name='eliminar_registros'),
    path('editar_registros/<int:registros_id>/', editar_registros, name='editar_registros'),
]
# Acá se llaman las funciones creadas en views.py para ser mostradas en el navegador
