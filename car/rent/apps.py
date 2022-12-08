from django.apps import AppConfig


class MyAppConfig(AppConfig):
    name = 'rent'

    def ready(self):
        import rent.signals