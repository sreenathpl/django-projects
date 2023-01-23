from . import views
from django.urls import path
app_name = 'appShopping'

urlpatterns = [
    path('',views.allCategory, name='allCategory'),
    path('<slug:c_slug>/',views.allCategory, name='allProductsCat'),
    path('<slug:c_slug>/<slug:p_slug>',views.allProducts, name='detailsProduct'),
    ]
