from django.urls import path, include

urlpatterns = [
    #path('usuarios/', include('usuarios.urls')),

    path('cuentas/', include('django.contrib.auth.urls')),
]
