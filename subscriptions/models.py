import datetime
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class SubscriptionStatus(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    paid_until = models.DateField(null=True, blank=True)

    def has_paid(self):
        current_date = datetime.date.today()

        return current_date < self.paid_until

    def __str__(self):
        return self.user.username
