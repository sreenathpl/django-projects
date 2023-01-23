from django.db import models
from appShopping.models import product

# Create your models here.
class cart(models.Model):
    cart_id=models.CharField(max_length=150, blank=True)
    date_added=models.DateField(auto_now_add=True)

    class Meta:
        db_table='cart'
        ordering=['date_added']

    def __str__(self):
        return self.cart_id

class cart_items(models.Model):
    products = models.ForeignKey(product,on_delete=models.CASCADE)
    cart = models.ForeignKey(cart,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'cart_items'

    def sub_total(self):
        return self.products.price * self.quantity

    def __str__(self):
        return self.products