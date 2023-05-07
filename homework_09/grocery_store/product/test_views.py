from django.test import TestCase
from .models import Category, Product


class TestViews(TestCase):
    def test_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_context(self):
        category = Category.objects.create(name='Чай')
        product = Product.objects.create(name='Гринфилд', category=category, weight=20, price=120)
        response = self.client.get('/')
        self.assertTrue('product' in response.context)
        self.assertTrue(response.context['product'].first().id, product.id)





