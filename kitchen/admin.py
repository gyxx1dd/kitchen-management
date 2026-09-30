from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from kitchen.models import DishType, Cook, Dish


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience", )
    fieldsets = UserAdmin.fieldsets + (
        ("Year of experience", {"fields": ("years_of_experience",)}),
    )

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "price", "dish_type_name", "cooks_username")

    def dish_type_name(self, obj):
        return obj.dish_type.name

    def cooks_username(self, obj):
        return list((cook.username for cook in obj.cooks.all()))