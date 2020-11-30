from django.contrib.postgres.fields import ArrayField
from django.db import models


class MealType(models.Model):
    meal_type = models.CharField(max_length=254)

    def __str__(self):
        return self.meal_type


class PlanLevel(models.Model):
    Difficulty = models.CharField(max_length=40)

    def __str__(self):
        return self.Difficulty


class Meal(models.Model):
    meal_type = models.ForeignKey(
        'MealType', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254, null=True, blank=True)
    calories = models.IntegerField(blank=True, null=True)
    ingredients = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    meal_img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class MealPlan(models.Model):
    name = models.CharField(max_length=254)
    plan_thumb_nail = models.ImageField(default='default-profile-img.png', upload_to='mealPlanThumbNails')
    length = models.CharField(max_length=100, default='7 Days')
    description = models.CharField(max_length=300, default="description pending")
    is_premium = models.BooleanField(default=True)
    difficulty_level = models.ForeignKey('PlanLevel', null=True, blank=True, on_delete=models.SET_NULL)
    vegetarian_friendly = models.BooleanField(default=False)
    Monday = models.ManyToManyField("Meal", related_name='+')
    Tuesday = models.ManyToManyField("Meal", related_name='+')
    wednesday = models.ManyToManyField("Meal", related_name='+')
    Thursday = models.ManyToManyField("Meal", related_name='+')
    Friday = models.ManyToManyField("Meal", related_name='+')
    Saturday = models.ManyToManyField("Meal", related_name='+')
    Sunday = models.ManyToManyField("Meal", related_name='+')

    def __str__(self):
        return self.name
