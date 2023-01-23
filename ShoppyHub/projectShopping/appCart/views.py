from django.shortcuts import render, redirect, get_object_or_404
from appShopping.models import product
from .models import cart, cart_items
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def _cart_id(request):
    cart_id=request.session.session_key
    if not cart:
        cart_id=request.session.create()
    return cart_id


def add_cart(request, product_id):
    cart_product = product.objects.get(id=product_id)
    try:
        create_cart = cart.objects.get(cart_id=_cart_id(request))
    except cart.DoesNotExist:
        create_cart = cart.objects.create(cart_id=_cart_id(request))
        create_cart.save()

    try:

        add_items_cart = cart_items.objects.get(products=cart_product, cart=create_cart)
        if add_items_cart.quantity < add_items_cart.products.stock:
            add_items_cart.quantity +=1
            add_items_cart.save()

    except cart_items.DoesNotExist:
        add_items_cart = cart_items.objects.create(products=cart_product,
                                               quantity=1,
                                               cart=create_cart)
        add_items_cart.save()

    return redirect('appCart:cart_details')


def cart_details(request, total=0,counter=0, items_cart=None):
    try:
        cart_id = cart.objects.get(cart_id=_cart_id(request))
        items_cart = cart_items.objects.filter(cart=cart_id, active=True)
        for item_cart in items_cart:
            total += (item_cart.products.price * item_cart.quantity)
            counter += item_cart.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',{'cart_items':items_cart,
                                       'total':total,
                                       'counter':counter})

def cart_remove(request, product_id):
    cartID = cart.objects.get(cart_id=_cart_id(request))
    products = get_object_or_404(product, id=product_id)
    cartItem = cart_items.objects.get(products = products, cart= cartID)
    if cartItem.quantity > 1:
        cartItem.quantity -= 1
        cartItem.save()
    else:
        cartItem.delete()
    return redirect('appCart:cart_details')

def cart_item_delete(request, product_id):
    cartID = cart.objects.get(cart_id=_cart_id(request))
    products = get_object_or_404(product, id=product_id)
    cartItem = cart_items.objects.get(products = products, cart= cartID)
    cartItem.delete()
    return redirect('appCart:cart_details')


