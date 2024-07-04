from django.apps import AppConfig


class AppUsuarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_usuario'

    # Se agrego para inicializar
    def ready(self):
        import app_usuario.signals
