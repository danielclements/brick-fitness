# Generated by Django 3.0.8 on 2020-11-30 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0013_auto_20201130_1356'),
        ('user_profiles', '0005_profile_active_meal_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='active_workout_plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='plans.WorkOutPlan'),
        ),
    ]
