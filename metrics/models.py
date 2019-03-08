from django.db import models


class Metric(models.Model):
    date = models.DateField()
    channel = models.CharField(max_length=30)
    country = models.CharField(max_length=2)
    os = models.CharField(max_length=10)
    impressions = models.IntegerField(default=0)
    clicks = models.IntegerField(default=0)
    installs = models.IntegerField(default=0)
    spend = models.DecimalField(max_digits=8, decimal_places=2)
    revenue = models.DecimalField(max_digits=8, decimal_places=2)
