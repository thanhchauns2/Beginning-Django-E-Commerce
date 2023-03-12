from django.shortcuts import get_object_or_404, redirect, render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from cart.forms import ProductAddToCartForm 
from cart import cart
from django.urls import reverse

from catalog.models import Category, Product

def index(request):
    page_title = 'Musical Instruments and Sheet Music for Musicians'
    return render(request, "catalog/index.html", {'page_title': page_title})
    # (template_name, locals(),
    # context_instance=RequestContext(request))


def show_category(request, slug):
    c = get_object_or_404(Category, slug=slug)
    products = c.product_set.all()
    page_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.meta_description
    return render(request, "catalog/category.html", {'c': c, 'products': products,
                                                     'page_title': page_title})

def show_product(request, slug):
    p = get_object_or_404(Product, slug=slug)
    categories = p.categories.all()
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description

    # need to evaluate the HTTP method
    if request.method == 'POST':
        # add to cart…create the bound form
        postdata = request.POST.copy()
        form = ProductAddToCartForm(request, postdata)
        #check if posted data is valid
        if form.is_valid():
            #add to cart and redirect to cart page
            cart.add_to_cart(request)
            # if test cookie worked, get rid of it
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            url = reverse('show_cart')
            return HttpResponseRedirect(url)
    else:
        # it’s a GET, create the unbound form. Note request as a kwarg
        form = ProductAddToCartForm(request=request, label_suffix=':')

    # assign the hidden input the product slug
    form.fields['slug'].widget.attrs['value'] = slug
    # set the test cookie on our first GET request
    request.session.set_test_cookie()

    context = {'p': p, 'categories': categories, 'page_title': page_title, 'form': form}
    return render(request, "catalog/product.html", context)