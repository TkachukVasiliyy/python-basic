from django.shortcuts import render
from .models import Product, Category
from django.views.generic import ListView, DetailView


def index_view(request):
    product = Product.objects.all()
    context = {
        'product': product
    }
    return render(request, 'grocery_store/index.html', context=context)


class CategoryListView(ListView):
    model = Category
    template_name = 'grocery_store/category_list.html'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'grocery_store/category_detail.html'