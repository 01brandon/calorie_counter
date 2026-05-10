from django.urls import path
from . import views

app_name = 'calorie_tracker'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_food, name='add_food'),
    path('delete/<int:item_id>/', views.delete_food, name='delete_food'),
    path('reset/', views.reset_daily, name='reset_daily'),
    path('food/<int:item_id>/', views.food_detail, name='food_detail'),
    path('history/', views.history, name='history'),
]