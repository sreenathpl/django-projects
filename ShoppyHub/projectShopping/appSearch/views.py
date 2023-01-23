from django.shortcuts import render
from appShopping.models import product
from django.db.models import Q

# Create your views here.
def product_search(request):
    # products = None
    # query = None
    # if 'q' in request.GET:
    query = request.GET.get('q')
    products = product.objects.filter(Q(name__contains=query) | Q(description__contains=query))

    print(query)
    print(products)
    return render(request,'search.html',{'query':query,'products':products})