from django.test import TestCase
from .models import Category, Product


class TestCategory(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Сухари')
        print('Начала теста')

    def tearDown(self):
        print('Конец теста')

    def test_init(self):
        self.assertEquals(self.category.name, 'Сухари')

    def test_str(self):
        self.assertEquals(str(self.category), 'Сухари')


