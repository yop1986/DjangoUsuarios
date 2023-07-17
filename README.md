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
    
#### Dependencias del proyecto
    
    asgiref==3.7.2
    Django==4.2.3
    mysqlclient==2.2.0
    sqlparse==0.4.4
    tzdata==2023.3

#### Comandos básicos

    (.venv) django-admin startproject <nombre proyecto>
    (.venv) python manage.py startapp <nombre app>
    (.venv) python manage.py makemigrations
    (.venv) python manage.py migrate <zero | #_name>
    (.venv) python manage.py showmigrations
    (.venv) python manage.py createsuperuser

#### Configuración inicial

_Settings_: Registro de librerias útilizadas (al inicio del archivo)

    import os
    from django.urls import reverse_lazy

_Settings_: Registro de aplicaciones

    INSTALLED_APPS = [
        ...
        'usuarios',
    ]

_Settings_: Configuración de directorios para plantillas

    TEMPLATES = [
        {
            ...
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
            ...
        },
    ]

_Settings_: Configuración de base de datos

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

_Settings_: Configuración de regionalización

    LANGUAGE_CODE = 'es-gt'
    TIME_ZONE = 'UTC'
    USE_I18N = True
    USE_TZ = True

_Settings_: Configuración de archivos Static

    STATICFILES_DIRS = (
        ('static', os.path.join(BASE_DIR, 'static/')),
    )
_**Se debe crear la carpeta 'static' en el directorio raiz del proyecto o donde se haya definido en la configuración anterior.**_

_Settings_: Configuraciones adicionales

    CONFIGURACION = {
        'sitio'     : "Nombre",
        'disp_admin': "Nombre del administrador",
        'mail_admin': "Correo",
    }
    APPS_DESC = {
        'usuarios': { # Detalle para acceder al modulo instalado desde el 'home'
            'nombre':       'Usuarios',
            'descripcion': 'Control de usuarios y permisos a las aplicaciones.',
            'enlace':       reverse_lazy('usuarios:index'),
            'imagen':       'usuarios_logo.png',
        }
    }
    AUTH_USER_MODEL = "usuarios.Usuario"


_urls.py_: Registro de urls de aplicaciones instaladas

    path('', include('usuarios.urls')),