from django.shortcuts import render
from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from credit.models import Credit
from credit.forms import CreditForm

def get_credits(request):
    credits = Credit.objects.all()
    paginator = Paginator(credits, 3)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)
    #return credits


def create_credit(request):
    if request.method == "POST":
        credit_form = CreditForm(request.POST)
        if credit_form.is_valid():
            data = credit_form.cleaned_data
            actual_objects = Credit.objects.filter(
                code=data["code"],
                description=data["description"],
                amount=data["amount"],
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"El limite de credito {data['code']} - {data['description']} ya está creado",
                )
            else:
                credit = Credit(
                    code=data["code"],
                    description=data["description"],
                    amount=data["amount"],
                )
                credit.save()
                messages.success(
                    request,
                    f"Limite de credito {data['code']} - {data['description']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"credits": get_credits(request)},
                template_name="credit/credit_list.html",
            )

    credit_form = CreditForm(request.POST)
    context_dict = {"form": credit_form}
    return render(
        request=request,
        context=context_dict,
        template_name="credit/credit_form.html",
    )


def credits(request):
    #credits = Credit.objects.all()

    #context_dict = {"credits": credits}

    return render(
        request=request,
        context={"credits": get_credits(request)},
        #context=context_dict,
        template_name="credit/credit_list.html",
    )
