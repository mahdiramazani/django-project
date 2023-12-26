from django.apps import AppConfig

class AcountappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.AcountApp'

    verbose_name = "کاربران"

    def ready(self):
        import apps.HomeApp.signals