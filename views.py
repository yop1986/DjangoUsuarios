from django.conf import settings
from django.utils.translation import gettext as _
from django.views.generic.base import ContextMixin, TemplateView

# Configuración del sitio web
class PersonalContextMixin(ContextMixin):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['config'] = settings.CONFIGURACION
        return context 

# PRIVATE VIEWS


# PUBLIC VIEWS
class Home(TemplateView, PersonalContextMixin):
    template_name = 'home.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = context['config']['sitio']
        context['apps'] = self.get_installed_apps()
        return context

    def get_installed_apps(self):
        mis_apps = []
        for app, info in settings.APPS_DESC.items():
            if app in settings.INSTALLED_APPS:
                mis_apps.append(info)

        return mis_apps


class Index(TemplateView, PersonalContextMixin):
    template_name = 'index.html'
    extra_context = {
        'title': _('Usuarios'),
    }
