# Create your views here.
from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


from customer.forms import CustomerForm
from customer.models import Customer


def get_customers(request):
    customers = Customer.objects.all()
    paginator = Paginator(customers, 3)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)



def create_customer(request):
    if request.method == "POST":
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            data = customer_form.cleaned_data
            actual_objects = Customer.objects.filter(
                code=data["code"],
                name=data["name"],
                email=data["email"],
                segment=data["segment"],
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"El cliente {data['code']} - {data['name']} ya está creado",
                )
            else:
                customer = Customer(
                    code=data["code"],
                    name=data["name"],
                    email=data["email"],
                    segment=data["segment"],
                )
                customer.save()
                messages.success(
                    request,
                    f"Cliente {data['code']} - {data['name']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"customers": get_customers(request)},
                template_name="customer/customer_list.html",
            )

    customer_form = CustomerForm(request.POST)
    context_dict = {"form": customer_form}
    return render(
        request=request,
        context=context_dict,
        template_name="customer/customer_form.html",
    )


def customers(request):
    return render(
        request=request,
        context={"customers": get_customers(request)},
        template_name="customer/customer_list.html",
    )
