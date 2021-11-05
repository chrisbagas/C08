from django.apps import AppConfig


class ProfileDashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profile_dashboard'

    def ready(self):
        import profile_dashboard.signals