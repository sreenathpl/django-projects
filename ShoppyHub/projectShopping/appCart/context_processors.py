from .models import cart, cart_items
from .views import _cart_id

def counter(request):
    item_count = 0
    if 'admin' in request.path:
        return  {}
    else:
        try:
            cartObjects = cart.objects.filter(cart_id=_cart_id(request))
            cartItems = cart_items.objects.all().filter(cart=cartObjects[:1])
            for items in cartItems:
                item_count += items.quantity

        except cart.DoesNotExist:
            item_count = 0
    return dict(item_count=item_count)