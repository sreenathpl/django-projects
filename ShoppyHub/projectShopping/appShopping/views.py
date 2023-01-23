from django.shortcuts import render, get_object_or_404
from .models import category, product
from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.
def shopping_home(request):
    return render(request,'index.html')

def allCategory(request, c_slug= None):
    c_page=None
    products_list=None
    if c_slug != None:
        c_page = get_object_or_404(category, slug= c_slug)
        products_list = product.objects.all().filter(category=c_page,
                                                available=True)
    else:
        products_list = product.objects.all().filter(available=True)

    paginator = Paginator(products_list,8)

    try:
        pages = int(request.GET.get('page','1'))
    except:
        pages = 1

    try:
        products = paginator.page(pages)
    except(EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request,"category.html",{'category':c_page,'product':products})

def allProducts(request, c_slug, p_slug):
    try:
        products = product.objects.get(category__slug=c_slug, slug=p_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':products})