from django.apps import AppConfig
from django.utils.translation import ugettext_lazy


class PluginApp(AppConfig):
    name = 'pretix_siteimprove'
    verbose_name = 'Siteimprove'

    class PretixPluginMeta:
        name = ugettext_lazy('Siteimprove')
        author = 'Mikkel Ricky'
        description = ugettext_lazy('Adds Siteimprove to Pretix')
        visible = True
        version = '1.0.0'

    def ready(self):
        from . import signals  # NOQA


default_app_config = 'pretix_siteimprove.PluginApp'
