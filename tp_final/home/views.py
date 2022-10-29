from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from customer.models import Customer
#from product.models import Product

def index(request):
    return render(
        request=request,
        context={},
        template_name="home/index.html",
    )
    
def search(request):
    search_param = request.GET["search_param"]
    print("search: ", search_param)
    context_dict = dict()
    if search_param:
        query = Q(name__contains=search_param)
        query.add(Q(code__contains=search_param), Q.OR)
        customers = Customer.objects.filter(query)
        context_dict.update(
            {
                "customers": customers,
                "search_param": search_param,
            }
        )
    return render(
        request=request,
        context=context_dict,
        template_name="home/index.html",
    )
    

from product.models import Product
    
def index(request):
    return render(
        request=request,
        context={},
        template_name="home/index.html",
    )
    
def search(request):
    search_param = request.GET["search_param"]
    print("search: ", search_param)
    context_dict = dict()
    if search_param:
        query = Q(description__contains=search_param)
        query.add(Q(code__contains=search_param), Q.OR)
        products = Product.objects.filter(query)
        context_dict.update(
            {
                "products": products,
                "search_param": search_param,
            }
        )
    return render(
        request=request,
        context=context_dict,
        template_name="home/index.html",
    )    