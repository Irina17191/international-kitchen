from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.models import DishType, Dish, Country, Cook


admin.site.register(DishType)
admin.site.register(Dish)
admin.site.register(Country)
admin.site.register(Cook, UserAdmin)