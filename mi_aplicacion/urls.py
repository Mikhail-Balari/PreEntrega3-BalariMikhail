from django.contrib import admin
from django.urls import path, include  
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mi_aplicacion/', include('mi_aplicacion.urls')),  # Agrega la URL de la aplicación
    path('insertar-datos/', views.insertar_datos, name='insertar_datos'),  # Agrega la nueva URL aquí
    # Agrega las siguientes dos líneas para las URLs de los archivos HTML
    path('exito/', views.exito, name='exito'),  # Ruta para la página de éxito
    path('buscar-producto/', views.buscar_producto, name='buscar_producto'),  # Ruta para la página de búsqueda
    path('resultados-busqueda/', views.resultados_busqueda, name='resultados_busqueda'),
]
