from django.contrib import admin
from .models import MealType, Meal, MealPlan


# Register your models here.
class MealTypeAdmin(admin.ModelAdmin):
    list_display = (
        'meal_type',
    )


class MealAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'meal_type',
        'calories',
        'ingredients',
        'meal_img',
    )


class MealPlanAdmin(admin.ModelAdmin):
    filter_horizontal = (
        'Monday',
        'Tuesday',
        'wednesday',
        'Thursday',
        'Friday',
        'Saturday',
        'Sunday',
    )


admin.site.register(MealType, MealTypeAdmin)
admin.site.register(Meal, MealAdmin)
admin.site.register(MealPlan, MealPlanAdmin)

