from django.shortcuts import render

from django.template import RequestContext
from cart import cart

def show_cart(request):
    cart_item_count = cart.cart_item_count(request)
    page_title = 'Shopping Cart'
    return render(request, "cart/cart.html", locals()) 