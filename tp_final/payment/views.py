# Create your views here.
from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from payment.models import Payment
from payment.forms import PaymentForm

def get_payments(request):
    payments = Payment.objects.all()
    paginator = Paginator(payments, 3)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)
    #return payments


def create_payment(request):
    if request.method == "POST":
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            data = payment_form.cleaned_data
            actual_objects = Payment.objects.filter(
                code=data["code"],
                name=data["name"],
                days=data["days"],
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"La condicion de pago {data['code']} - {data['name']} ya está creado",
                )
            else:
                payment = Payment(
                    code=data["code"],
                    name=data["name"],
                    days=data["days"],
                )
                payment.save()
                messages.success(
                    request,
                    f"La condicion de pago {data['code']} - {data['name']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"payments": get_payments(request)},
                template_name="payment/payment_list.html",
            )

    payment_form = PaymentForm(request.POST)
    context_dict = {"form": payment_form}
    return render(
        request=request,
        context=context_dict,
        template_name="payment/payment_form.html",
    )


def payments(request):
    #payments = Payment.objects.all()

    #context_dict = {"payments": payments}

    return render(
        request=request,
        context={"payments": get_payments(request)},
        #context=context_dict,
        template_name="payment/payment_list.html",
    )
