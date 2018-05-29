from django.db import models
from django.contrib.auth.models import User


class Month(models.Model):
    month = models.CharField(max_length = 10)
    total_expenditure = models.IntegerField(default = 0)
    total_income = models.IntegerField(default = 0)

    def __str__(self):
        return self.month


class Daily_info(models.Model):
    expenditure = models.IntegerField(default = 0)
    income = models.IntegerField(default = 0)
    description = models.CharField(max_length = 100)
    date = models.IntegerField(default = 0)
    account = models.ForeignKey(Month, null=True, related_name = 'account')
