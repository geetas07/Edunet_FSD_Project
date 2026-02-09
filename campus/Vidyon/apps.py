from django.apps import AppConfig


class VidyonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Vidyon'

    def ready(self):
        import Vidyon.signals
