from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class ISO(models.Model):
    value = models.CharField(max_length=2)

    def __str__(self):
        return self.value

class Site(models.Model):
    name = models.CharField(max_length=128)
    year = models.PositiveIntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    states = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    iso = models.ForeignKey(ISO, on_delete=models.CASCADE, null=True)
    area_hect = models.FloatField(null=True)
    description = models.TextField()
    justification = models.TextField()

    def __str__(self):
        return self.name

