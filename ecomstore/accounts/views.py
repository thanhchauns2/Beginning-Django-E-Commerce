from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from checkout.models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from accounts.forms import UserProfileForm
from accounts import profile
from django.urls import reverse


def register(request):
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = UserCreationForm(postdata)
        if form.is_valid():
            form.save()
            un = postdata.get('username', '')
            pw = postdata.get('password1', '')
            from django.contrib.auth import login, authenticate
            new_user = authenticate(username=un, password=pw)
            if new_user and new_user.is_active:
                login(request, new_user)
                url = reverse('my_account')
                return HttpResponseRedirect(url)
    else:
        form = UserCreationForm()
    page_title = 'User Registration'
    context = {'page_title': page_title, 'form': form}
    return render(request, "registration/register.html", context)


@login_required
def my_account(request):
    page_title = 'My Account'
    orders = Order.objects.filter(user=request.user)
    name = request.user.username
    context = {'page_title': page_title, 'name': name, 'orders': orders}
    return render(request, "registration/my_account.html", context)


@login_required
def order_details(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    page_title = 'Order Details for Order #' + order_id
    order_items = OrderItem.objects.filter(order=order)
    context = {'page_title': page_title, 'order_items': order_items, 'order': order}
    return render(request, "registration/order_details.html", context)

@login_required
def order_info(request):
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = UserProfileForm(postdata)
        if form.is_valid():
            profile.set(request)
            url = urlresolvers.reverse('my_account')
            return HttpResponseRedirect(url)
    else:
        user_profile = profile.retrieve(request)
        form = UserProfileForm(instance=user_profile)
    page_title = 'Edit Order Information'
    context = {'page_title': page_title, 'form' : form}
    return render(request, "registration/order_info.html", context)
