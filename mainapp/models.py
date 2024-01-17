from django.db import models

# Create your models here.

class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    key_skills = models.TextField(blank=True, null=True)
    salary_from = models.FloatField(blank=True, null=True)
    salary_to = models.FloatField(blank=True, null=True)
    salary_currency = models.CharField(max_length=10, blank=True, null=True)
    area_name = models.CharField(max_length=255, blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

class CurrencyRate(models.Model):
    date = models.DateField(unique=True)
    BYR = models.FloatField(null=True, blank=True)
    USD = models.FloatField(null=True, blank=True)
    EUR = models.FloatField(null=True, blank=True)
    KZT = models.FloatField(null=True, blank=True)
    UAH = models.FloatField(null=True, blank=True)
    AZN = models.FloatField(null=True, blank=True)
    KGS = models.FloatField(null=True, blank=True)
    UZS = models.FloatField(null=True, blank=True)
    GEL = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.date)