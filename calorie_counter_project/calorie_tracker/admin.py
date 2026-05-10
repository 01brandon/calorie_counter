from django.contrib import admin
from .models import FoodItem


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    """Admin interface configuration for FoodItem model."""
    
    list_display = [
        'name',
        'calories',
        'date_added',
        'created_at',
    ]
    
    list_filter = [
        'date_added',
        'created_at',
        'calories',
    ]
    
    search_fields = [
        'name',
    ]
    
    readonly_fields = [
        'created_at',
        'updated_at',
    ]
    
    fieldsets = (
        ('Food Information', {
            'fields': ('name', 'calories')
        }),
        ('Dates', {
            'fields': ('date_added', 'created_at', 'updated_at')
        }),
    )
    
    ordering = ['-date_added', '-created_at']
    
    date_hierarchy = 'date_added'
    
    def get_queryset(self, request):
        """Optimize queryset with select_related and prefetch_related."""
        queryset = super().get_queryset(request)
        return queryset.order_by('-date_added', '-created_at')