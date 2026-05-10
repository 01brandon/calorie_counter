from django import forms
from .models import FoodItem
from datetime import date


class FoodItemForm(forms.ModelForm):
    """Form for creating and updating food items."""
    
    class Meta:
        """Meta options for FoodItemForm."""
        model = FoodItem
        fields = ['name', 'calories', 'date_added']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter food item name (e.g., Apple, Chicken Breast)',
                'maxlength': '255',
                'required': True,
            }),
            'calories': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter number of calories',
                'min': '0',
                'required': True,
                'type': 'number',
            }),
            'date_added': forms.DateInput(attrs={
                'class': 'w-full px-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500',
                'type': 'date',
                'max': date.today().isoformat(),
            }),
        }
    
    def clean_name(self):
        """Validate the food item name."""
        name = self.cleaned_data.get('name', '').strip()
        if not name:
            raise forms.ValidationError("Food item name cannot be empty.")
        if len(name) > 255:
            raise forms.ValidationError("Food item name must be 255 characters or less.")
        return name
    
    def clean_calories(self):
        """Validate the calorie value."""
        calories = self.cleaned_data.get('calories')
        if calories is None:
            raise forms.ValidationError("Please enter a calorie value.")
        if calories < 0:
            raise forms.ValidationError("Calories cannot be negative.")
        if calories > 10000:
            raise forms.ValidationError("Calorie value seems too high. Please verify.")
        return calories
    
    def clean_date_added(self):
        """Validate the date added."""
        date_added = self.cleaned_data.get('date_added')
        if date_added > date.today():
            raise forms.ValidationError("You cannot add food items for future dates.")
        return date_added


class DateFilterForm(forms.Form):
    """Form for filtering food items by date."""
    
    date = forms.DateField(
        initial=date.today,
        widget=forms.DateInput(attrs={
            'class': 'px-4 py-2 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500',
            'type': 'date',
        }),
        required=False,
        label='Select Date'
    )