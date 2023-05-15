from django.contrib import admin
from .models import Category, Card, Counterparty, Product

# Register your models here.
admin.site.register(Category)
admin.site.register(Card)
admin.site.register(Counterparty)
admin.site.register(Product)
