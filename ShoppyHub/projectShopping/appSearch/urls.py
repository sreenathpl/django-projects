from . import views
from django.urls import path
app_name = 'search_app'

urlpatterns = [
    path('search/',views.product_search,name='product_search'),
]
