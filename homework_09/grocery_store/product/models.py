from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('name', max_length=164)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    weight = models.IntegerField(verbose_name='weight')
    price = models.IntegerField(verbose_name='price')


#Карточка ТП, Карточка ТП и поставщик
    def count_product_types(self):
        return self.category.count()


class Card(models.Model):
    text = models.TextField(blank=True)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Counterparty(models.Model):
    name = models.CharField(max_length=128, unique=True)
    product = models.ManyToManyField(Product)

    def __str__(self):
        return self.name

