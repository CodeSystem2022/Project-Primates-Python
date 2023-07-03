from django.contrib import admin
from django.urls import path, include  # importamos el include para poder crear las rutas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('registros.urls'))

]
