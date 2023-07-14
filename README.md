# DjangoUsuarios
Modulo de usuarios django para mis aplicaciones

## Historial de versiones

|Fecha     |Descripción          |
|----------|:-------------------:|
|12/07/2023|Creación del paquete.|

## Validación de paquetes desactualizados

    pip list --outdated
    pip install --upgrade <paquetes>

Creación y uso de un ambiente virtual

    virtualenv .venv
    .venv\Scripts\activate.bat
    (.venv) pip install django mysqlclient

### Instalación y configuración Django
    
Dependencias del proyecto
    
    asgiref==3.7.2
    Django==4.2.3
    mysqlclient==2.2.0
    sqlparse==0.4.4
    tzdata==2023.3

Comandos básicos

    (.venv) django-admin startproject <nombre proyecto>
    (.venv) python manage.py startapp <nombre app>
    (.venv) python manage.py makemigrations
    (.venv) python manage.py migrate <zero | #_name>
    (.venv) python manage.py showmigrations
    (.venv) python manage.py createsuperuser

Archivo _Settings_ del proyecto:

    # Registro de librerias útilizadas (al inicio del archivo)
    import os

    # Registro de aplicaciones
    INSTALLED_APPS = [
        ...
        'usuarios',
    ]

    # Configuración de directorios para plantillas
    TEMPLATES = [
        {
            ...
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
            ...
        },
    ]

    # Configuración de base de datos
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": "<bbdd>",
            "USER": "<usuario>",
            "PASSWORD": "<contraseña>",
            "HOST": "<ip | nombre>",
            "PORT": "<puerto>",
        }
    }

    # Configuración de regionalización
    LANGUAGE_CODE = 'es-gt'
    TIME_ZONE = 'UTC'
    USE_I18N = True
    USE_TZ = True

    # Configuración de archivos Static
    STATICFILES_DIRS = (
        ('static', '/home/djangoenv/bin/mysuperapp/static'),
    )
    
    # Configuraciones adicionales
    AUTH_USER_MODEL = "usuarios.Usuario"

Archivo _urls.py_ del proyecto:
    
    #Se registran las urls de esta app
    path('usuarios/', include('usuarios.urls')),