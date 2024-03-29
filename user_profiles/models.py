from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from plans.models import MealPlan, WorkOutPlan


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11, null=True, blank=True, default="00000000000")
    profile_img = models.ImageField(default='default-profile-img.png', upload_to='profile_pics')
    subscription_premium = models.BooleanField(default=False)
    active_meal_plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE, null=True, blank=True)
    active_workout_plan = models.ForeignKey(WorkOutPlan, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


