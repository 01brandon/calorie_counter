from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib import messages
from django.db.models import Sum
from datetime import date, timedelta
import json
from .models import FoodItem
from .forms import FoodItemForm, DateFilterForm


def index(request):
    """Display the main calorie tracker page with today's food items."""
    today = date.today()
    today_items = FoodItem.objects.filter(date_added=today).order_by('-created_at')
    
    total_calories = today_items.aggregate(total=Sum('calories'))['total'] or 0
    
    form = FoodItemForm()
    
    seven_days_ago = today - timedelta(days=6)
    daily_data = []
    
    for i in range(7):
        current_date = seven_days_ago + timedelta(days=i)
        daily_total = FoodItem.objects.filter(
            date_added=current_date
        ).aggregate(total=Sum('calories'))['total'] or 0
        daily_data.append({
            'date': current_date.strftime('%a %m/%d'),
            'total': daily_total
        })
    
    context = {
        'today_items': today_items,
        'total_calories': total_calories,
        'form': form,
        'daily_data': json.dumps(daily_data),
        'today': today,
    }
    
    return render(request, 'index.html', context)


@require_http_methods(["POST"])
def add_food(request):
    """Handle the addition of a new food item via POST request."""
    form = FoodItemForm(request.POST)
    
    if form.is_valid():
        form.save()
        messages.success(
            request,
            f"{form.cleaned_data['name']} ({form.cleaned_data['calories']} cal) added successfully!"
        )
        return redirect('index')
    else:
        today = date.today()
        today_items = FoodItem.objects.filter(date_added=today).order_by('-created_at')
        total_calories = today_items.aggregate(total=Sum('calories'))['total'] or 0
        
        seven_days_ago = today - timedelta(days=6)
        daily_data = []
        
        for i in range(7):
            current_date = seven_days_ago + timedelta(days=i)
            daily_total = FoodItem.objects.filter(
                date_added=current_date
            ).aggregate(total=Sum('calories'))['total'] or 0
            daily_data.append({
                'date': current_date.strftime('%a %m/%d'),
                'total': daily_total
            })
        
        context = {
            'today_items': today_items,
            'total_calories': total_calories,
            'form': form,
            'daily_data': json.dumps(daily_data),
            'today': today,
        }
        
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, f"{field}: {error}")
        
        return render(request, 'index.html', context)


@require_http_methods(["POST"])
def delete_food(request, item_id):
    """Handle the deletion of a food item."""
    food_item = get_object_or_404(FoodItem, id=item_id)
    item_name = food_item.name
    food_item.delete()
    messages.success(request, f"{item_name} removed from your list.")
    return redirect('index')


@require_http_methods(["POST"])
def reset_daily(request):
    """Handle the reset of today's calorie count."""
    today = date.today()
    count = FoodItem.objects.filter(date_added=today).count()
    FoodItem.objects.filter(date_added=today).delete()
    messages.success(request, f"Reset complete! Removed {count} item(s) from today's list.")
    return redirect('index')


def food_detail(request, item_id):
    """Display detailed information about a specific food item."""
    food_item = get_object_or_404(FoodItem, id=item_id)
    context = {
        'food_item': food_item,
    }
    return render(request, 'food_detail.html', context)


def history(request):
    """Display the history of food items consumed."""
    form = DateFilterForm(request.GET or None)
    
    if form.is_valid() and form.cleaned_data.get('date'):
        selected_date = form.cleaned_data['date']
    else:
        selected_date = date.today()
    
    items = FoodItem.objects.filter(date_added=selected_date).order_by('-created_at')
    total_calories = items.aggregate(total=Sum('calories'))['total'] or 0
    
    all_items = FoodItem.objects.all()
    average_daily = 0
    if all_items.exists():
        days_with_data = all_items.values('date_added').distinct().count()
        if days_with_data > 0:
            total_all = all_items.aggregate(total=Sum('calories'))['total'] or 0
            average_daily = total_all // days_with_data
    
    context = {
        'items': items,
        'total_calories': total_calories,
        'selected_date': selected_date,
        'form': form,
        'average_daily': average_daily,
    }
    
    return render(request, 'history.html', context)