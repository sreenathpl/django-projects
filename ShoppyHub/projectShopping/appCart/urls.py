from . import views
from django.urls import path
app_name = 'appCart'

urlpatterns = [
    path('add_cart/<int:product_id>/',views.add_cart, name='add_cart'),
    path('cart_details/', views.cart_details, name="cart_details"),
    path('cart_remove/<int:product_id>/',views.cart_remove, name='cart_remove'),
    path('cart_item_delete/<int:product_id>/',views.cart_item_delete, name='cart_item_delete'),
    ]