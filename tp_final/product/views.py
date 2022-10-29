# Create your views here.
from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from product.models import Product
from product.forms import ProductForm

def get_products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 3)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)
    #return products


def create_product(request):
    if request.method == "POST":
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            data = product_form.cleaned_data
            actual_objects = Product.objects.filter(
                code=data["code"],
                description=data["description"],
                unit_sales=data["unit_sales"],
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"El producto {data['code']} - {data['description']} ya está creado",
                )
            else:
                product = Product(
                    code=data["code"],
                    description=data["description"],
                    unit_sales=data["unit_sales"],
                )
                product.save()
                messages.success(
                    request,
                    f"El producto {data['code']} - {data['description']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"products": get_products(request)},
                template_name="product/product_list.html",
            )

    product_form = ProductForm(request.POST)
    context_dict = {"form": product_form}
    return render(
        request=request,
        context=context_dict,
        template_name="product/product_form.html",
    )


def products(request):
    #products = Product.objects.all()

    #context_dict = {"products": products}

    return render(
        request=request,
        context={"products": get_products(request)},
        #context=context_dict,
        template_name="product/product_list.html",
    )
