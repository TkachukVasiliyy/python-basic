from django.shortcuts import render
from products.models import Product

def main_page(request):
    product = Product.objects.all()
    context = {
        'product': product
    }
    return render(request, 'products/index.html', context=context)
