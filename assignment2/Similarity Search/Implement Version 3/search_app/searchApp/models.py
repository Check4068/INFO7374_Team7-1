from django.db import models

# Create your models here.


class Car(models.Model):
    similarity = models.DecimalField(max_digits=5, decimal_places=4)
    master_pi = models.CharField(max_length=255, blank=True)
    similar_pi = models.CharField(max_length=255, blank=True)


class Neighbor(models.Model):
    similarity = models.DecimalField(max_digits=5, decimal_places=4)
    master_pi = models.CharField(max_length=255, blank=True)
    master_url = models.CharField(max_length=255, blank=True)
    similar_pi = models.CharField(max_length=255, blank=True)
    similar_url = models.CharField(max_length=255, blank=True)
