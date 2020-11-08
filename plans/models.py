from django.contrib.postgres.fields import ArrayField
from django.db import models


# class ChessBoard(models.Model):
#     board = ArrayField(
#         ArrayField(
#             models.CharField(max_length=10, blank=True),
#             size=8,
#         ),
#         size=8,
#     )


class MealType(models.Model):
    meal_type = models.CharField(max_length=254)

    def __str__(self):
        return self.meal_type


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
    length = models.CharField(max_length=100, default='7 Days')
    Monday = models.ManyToManyField("Meal", related_name='+')
    Tuesday = models.ManyToManyField("Meal", related_name='+')
    wednesday = models.ManyToManyField("Meal", related_name='+')
    Thursday = models.ManyToManyField("Meal", related_name='+')
    Friday = models.ManyToManyField("Meal", related_name='+')
    Saturday = models.ManyToManyField("Meal", related_name='+')
    Sunday = models.ManyToManyField("Meal", related_name='+')

    def __str__(self):
        return self.name
