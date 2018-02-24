from django.db import models

# Create your models here.

# Model Region
class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return ' %s %s' % (self.id, self.name)

    class Meta:
        db_table = 'region'
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'

# Model City
class City(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return ' %s %s %s' % (self.id, self.name, self.region)

    class Meta:
        db_table = 'city'
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

# Model Category
class Category(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return ' %s %s' % (self.id, self.name)

    class Meta:
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

# Model Status
class Status(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return ' %s %s' % (self.id, self.name)

    class Meta:
        db_table = 'status'
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'

# class User(models.Model) :
