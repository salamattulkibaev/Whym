from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return ' %s' % (self.name)

    class Meta:
        db_table = 'region'
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'

class City(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return ' %s' % (self.name)

    class Meta:
        db_table = 'city'
        verbose_name = 'City'
        verbose_name_plural = 'Cities'