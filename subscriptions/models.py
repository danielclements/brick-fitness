from django.db import models
from django.contrib.auth.models import User


# no longer in use
# Moved from subscription service to one time payment
# as ran out of time due to project submission date
# Future updates will include the subscription plan
class StripeCustomer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    paid_until = models.DateField(null=True, blank=True)

