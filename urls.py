from django.urls import path, include

from .views import Home, Index

app_name = 'usuarios'

urlpatterns = [
    #path('usuarios/', include('usuarios.urls')),
    path('', Home.as_view(), name='home'),
    path('usuarios/', Index.as_view(), name='index'),

    path('usuarios/', include('django.contrib.auth.urls')),
]
