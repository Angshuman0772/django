from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        # Import the signals module to ensure signal handlers are connected
        # This is necessary because Django does not automatically discover signal handlers
        # The import statement ensures that the module is loaded and the signal handlers are registered
        import users.signals