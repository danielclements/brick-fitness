# Generated by Django 3.0.8 on 2020-11-30 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0012_workout_workoutplan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workoutplan',
            old_name='ame',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='workoutplan',
            name='plan_thumb_nail',
            field=models.ImageField(default='Workout-plan-Free.jpg', upload_to='WorkOutThumbNails'),
        ),
    ]
