from django.contrib import admin

from .models import Food, FoodType


admin.site.register(Food)
admin.site.register(FoodType)
