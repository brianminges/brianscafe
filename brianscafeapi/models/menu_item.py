from django.db import models

class MenuItem(models.Model):
    """Creates a model for each Menu Item"""
    name = models.CharField(max_length=100)
    heat_level = models.CharField(max_length=2, blank=True, null=True)
    about = models.CharField(max_length=500)
    cost = models.DecimalField(decimal_places=2, max_digits=5)