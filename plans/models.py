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


class Workout(models.Model):
    name = models.CharField(max_length=50)
    unit = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class WorkOutPlan(models.Model):
    name = models.CharField(max_length=254)
    plan_thumb_nail = models.ImageField(default='Workout-plan-Free.jpg', upload_to='WorkOutThumbNails')
    length = models.CharField(max_length=100, default='7 Days')
    description = models.CharField(max_length=300, default="description pending")
    difficulty_level = models.ForeignKey('PlanLevel', null=True, blank=True, on_delete=models.SET_NULL)
    is_premium = models.BooleanField(default=True)
    Monday2 = models.ManyToManyField("Workout", related_name='+')
    Tuesday2 = models.ManyToManyField("Workout", related_name='+')
    wednesday2 = models.ManyToManyField("Workout", related_name='+')
    Thursday2 = models.ManyToManyField("Workout", related_name='+')
    Friday2 = models.ManyToManyField("Workout", related_name='+')
    Saturday2 = models.ManyToManyField("Workout", related_name='+')
    Sunday2 = models.ManyToManyField("Workout", related_name='+')

    def __str__(self):
        return self.name


class MealPlan(models.Model):
    name = models.CharField(max_length=254)
    plan_thumb_nail = models.ImageField(default='Meal Plan Premium.jpg', upload_to='mealPlanThumbNails')
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
