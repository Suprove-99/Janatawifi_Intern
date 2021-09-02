from django.db import models
from django.urls import reverse


# Create your models here.
class MyModel(models.Model):
    date = models.DateField()
    trade_code = models.CharField(max_length=254)
    high = models.FloatField()
    low = models.FloatField()
    open = models.FloatField()
    close = models.FloatField()
    volume = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('home_')