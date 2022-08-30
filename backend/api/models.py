from django.db import models

# Create your models here.

class CarPrice(models.Model):

    ENGINE_LOCATION_CHOICES = (
        ('Front', 'Front'),
        ('Rear', 'Rear')
    )
    DRIVE_WHEELS_CHOICES = (
        ('Fwd', 'Fwd'),
        ('Rwd', 'Rwd'),
        ('4wd', '4wd')
    )

    curb_weight = models.IntegerField(default=0)
    engine_size = models.IntegerField(default=0)
    horsepower = models.IntegerField(default=0)
    city_highway_mpg = models.FloatField(default=0)
    wheel_base = models.FloatField(default=0)
    size = models.FloatField(default=0)
    engine_location = models.CharField(max_length=15, choices=ENGINE_LOCATION_CHOICES)
    drive_wheels = models.CharField(max_length=15, choices=DRIVE_WHEELS_CHOICES)
    price = models.FloatField(default=0)
