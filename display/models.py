from django.db import models


# Create your models here.

class Temperature(models.Model):
    sensor_id = models.CharField(max_length=11)
    temperature = models.FloatField()
    create_time = models.DateTimeField(auto_now_add=True)


class Pressure(models.Model):
    sensor_id = models.CharField(max_length=11)
    pressure = models.FloatField()
    create_time = models.DateTimeField(auto_now_add=True)


class Gas(models.Model):
    sensor_id = models.CharField(max_length=11)
    gas = models.FloatField()
    create_time = models.DateTimeField(auto_now_add=True)
