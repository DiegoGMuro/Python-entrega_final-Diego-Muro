from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from customer.models import Customer
from product.models import Product
from payment.models import Payment

def index(request):
    return render(
        request=request,
        context={},
        template_name="home/index.html",
    )
    
def searchc(request):
    search_customer = request.GET["search_customer"]
    print("searchc: ", search_customer)
    context_dict = dict()
    if search_customer:
        query = Q(name__contains=search_customer)
        query.add(Q(code__contains=search_customer), Q.OR)
        customers = Customer.objects.filter(query)
        context_dict.update(
            {
                "customers": customers,
                "search_customer": search_customer,
            }
        )
    return render(
        request=request,
        context=context_dict,
        template_name="home/index.html",
    )
    
    
def searchp(request):
    search_product = request.GET["search_product"]
    print("searchp: ", search_product)
    context_dict = dict()
    if search_product:
        query = Q(description__contains=search_product)
        query.add(Q(code__contains=search_product), Q.OR)
        products = Product.objects.filter(query)
        context_dict.update(
            {
                "products": products,
                "search_product": search_product,
            }
        )
    return render(
        request=request,
        context=context_dict,
        template_name="home/index.html",
    )    