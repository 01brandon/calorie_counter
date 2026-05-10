from django.db import models
from django.core.validators import MinValueValidator
from datetime import date


class FoodItem(models.Model):
    """
    Model representing a food item with calorie information.
    
    Attributes:
        name (str): The name of the food item
        calories (int): The number of calories in the food item
        date_added (date): The date the food item was added (defaults to today)
        created_at (datetime): Timestamp when the record was created
        updated_at (datetime): Timestamp when the record was last updated
    """
    
    name = models.CharField(
        max_length=255,
        help_text="Name of the food item"
    )
    calories = models.PositiveIntegerField(
        validators=[MinValueValidator(0)],
        help_text="Number of calories in this food item"
    )
    date_added = models.DateField(
        default=date.today,
        help_text="Date when this food item was consumed"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the record was created"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Timestamp when the record was last updated"
    )
    
    class Meta:
        """Meta options for FoodItem model."""
        ordering = ['-date_added', '-created_at']
        verbose_name = "Food Item"
        verbose_name_plural = "Food Items"
        indexes = [
            models.Index(fields=['date_added']),
            models.Index(fields=['created_at']),
        ]
    
    def __str__(self):
        """String representation of the FoodItem."""
        return f"{self.name} ({self.calories} cal)"
    
    @staticmethod
    def get_today_total():
        """Calculate the total calories consumed today."""
        today_items = FoodItem.objects.filter(date_added=date.today())
        return sum(item.calories for item in today_items)
    
    @staticmethod
    def get_items_by_date(target_date):
        """Get all food items for a specific date."""
        return FoodItem.objects.filter(date_added=target_date)