# Create your views here.
from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


from credit.forms import CreditForm
from credit.models import Credit


def get_credits(request):
    credits = Credit.objects.all()
    paginator = Paginator(credits, 3)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)
    #return credits
    
def credits(request):
    return render(
        request=request,
        context={"credit_list": get_credits(request)},
        template_name="credit/credit_list.html",
    )


def credit_create(request):                               # reemplazo de create_credit por credit_create
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
            if not actual_objects:
                credit = Credit(
                    code=data["code"],
                    description=data["description"],
                    amount=data["amount"],                      
                )
                credit.save()
                messages.success(
                    request,
                    f"Credit {data['code']} - {data['description']} creado exitosamente!",
                )
                return render(
                    request=request,
                    context={"credit_list": get_credits(request)},
                    template_name="credit/credit_list.html",
                )
            else:                
                messages.error(
                    request,
                    f"El limite de credito {data['code']} - {data['description']} ya está creado",
                )

    credit_form = CreditForm(request.POST)
    context_dict = {"form": credit_form}
    return render(
        request=request,
        context=context_dict,
        template_name="credit/credit_form.html",
    )


def credit_detail(request, pk: int):
    return render(
        request=request,
        context={"credit": Credit.objects.get(pk=pk)},
        template_name="credit/credit_detail.html",
    )


def credit_update(request, pk: int):
    credit = Credit.objects.get(pk=pk)

    if request.method == "POST":
        credit_form = CreditForm(request.POST)
        if credit_form.is_valid():
            data = credit_form.cleaned_data
            credit.code = data["code"]
            credit.description = data["description"]
            credit.amount = data["amount"]
            credit.save()

            return render(
                request=request,
                context={"credit": credit},
                template_name="credit/credit_detail.html",
            )

    credit_form = CreditForm(model_to_dict(credit))
    context_dict = {
        "credit": credit,
        "form": credit_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name="credit/credit_form.html",
    )


def credit_delete(request, pk: int):
    credit = Credit.objects.get(pk=pk)
    if request.method == "POST":
        credit.delete()

        credits = Credit.objects.all()
        context_dict = {"credit_list": credits}
        return render(
            request=request,
            context=context_dict,
            template_name="credit/credit_list.html",
        )

    context_dict = {
        "credit": credit,
    }
    return render(
        request=request,
        context=context_dict,
        template_name="credit/credit_confirm_delete.html",
    )


from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from credit.models import Credit


class CreditListView(ListView):
    model = Credit
    paginate_by = 3


class CreditDetailView(DetailView):
    model = Credit
    fields = ["code", "description", "amount" ]


class CreditCreateView(CreateView):
    model = Credit
    success_url = reverse_lazy("credit:credit-list")

    form_class = CreditForm
    

    def form_valid(self, form):
        """Filter to avoid duplicate credits"""
        data = form.cleaned_data
        actual_objects = Credit.objects.filter(
            code=data["code"], description=data["description"]
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"El limite de credito {data['code']} - {data['description']} ya está creado",
            )
            form.add_error("description", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"El limite de credito {data['code']} - {data['description']} creado exitosamente!",
            )
            return super().form_valid(form)


class CreditUpdateView(UpdateView):
    model = Credit
    fields = ["code", "description", "amount"]

    def get_success_url(self):
        credit_id = self.kwargs["pk"]
        return reverse_lazy("credit:credit-detail", kwargs={"pk": credit_id})


class CreditDeleteView(DeleteView):
    model = Credit
    success_url = reverse_lazy("credit:credit-list")


