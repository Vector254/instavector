from django.apps import AppConfig


class InstavectorConfig(AppConfig):
    name = 'instavector'

    def ready(self):
        import users.signals
