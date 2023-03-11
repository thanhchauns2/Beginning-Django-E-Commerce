from django.shortcuts import get_object_or_404, render
from django.template import RequestContext

from catalog.models import Category, Product

def index(request):
    template_name="catalog/index.html"
    page_title = 'Musical Instruments and Sheet Music for Musicians'
    return render(request, template_name, {'page_title': page_title})

def show_category(request, slug):
    template_name="catalog/category.html"
    c = get_object_or_404(Category, slug=slug)
    products = c.product_set.all()
    page_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.meta_description
    return render(request, template_name, locals())

def show_product(request, slug):
    template_name="catalog/product.html"
    p = get_object_or_404(Product, slug=slug)
    categories = p.categories.filter(is_active=True)
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description
    return render(request, template_name, locals())