from django.shortcuts import render,redirect
from . import views
from store.models import Product
from .models import cart,CartItem


# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = cart.objects.get(cart_id=_cart_id(request))
    except cart.DoesNotExist:
        cart = cart.objects.create(
        cart_id = _cart_id(request)
        )

        cart.save()

    try:
        cart_item = CartItem.objects.get(product=product,cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
        product = product,
        quanity = 1,
        cart = cart,
        )
        cart_item.save()
    return redirect('cart')

def cart(request):
    return render(request,'store/cart.html')