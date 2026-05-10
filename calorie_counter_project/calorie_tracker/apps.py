from django.apps import AppConfig


class CalorieTrackerConfig(AppConfig):
    """Configuration for the calorie_tracker app."""
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'calorie_tracker'
    verbose_name = 'Calorie Tracker'
    
    def ready(self):
        """Perform initialization when the app is ready."""
        pass