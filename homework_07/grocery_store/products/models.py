from django.db import models


class Product(models.Model):
    name = models.CharField('name', max_length=164)
    weight = models.IntegerField(verbose_name='weight')
    price = models.IntegerField(verbose_name='price')

