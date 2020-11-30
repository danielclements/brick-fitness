from django.contrib import admin
from .models import MealType, Meal, MealPlan, PlanLevel


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


class PlanLevelAdmin(admin.ModelAdmin):
    list_display = (
        'Difficulty',
    )


admin.site.register(MealType, MealTypeAdmin)
admin.site.register(Meal, MealAdmin)
admin.site.register(MealPlan, MealPlanAdmin)
admin.site.register(PlanLevel, PlanLevelAdmin)


