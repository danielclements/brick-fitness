from django.db import models


# models
class Product(models.Model):

    name = models.CharField(max_length=50, null=False, blank=False)
    friendly_name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
