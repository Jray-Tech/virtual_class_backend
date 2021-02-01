from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals

# to get this to work i had to add a code to __init__.py to let it know to use this as default_app_config
# please see code below
# default_app_config = 'users.apps.UsersConfig'

