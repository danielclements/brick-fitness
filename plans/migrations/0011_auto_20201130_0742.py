# Generated by Django 3.0.8 on 2020-11-30 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0010_mealplan_plan_thumb_nail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealplan',
            name='plan_thumb_nail',
            field=models.ImageField(default='Meal Plan Premium.jpg', upload_to='mealPlanThumbNails'),
        ),
    ]