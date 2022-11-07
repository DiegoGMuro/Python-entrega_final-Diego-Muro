# Create your views here.
from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from payment.forms import PaymentForm
from payment.models import Payment


def get_payments(request):
    payments = Payment.objects.all()
    paginator = Paginator(payments, 3)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)
    #return payments
    
def payments(request):
    return render(
        request=request,
        context={"payment_list": get_payments(request)},
        template_name="payment/payment_list.html",
    )    
    


def payment_create(request):                         # reemplazo de create_payment por payment_create
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
            if not actual_objects:
                payment = Payment(
                    code=data["code"],
                    name=data["name"],
                    days=data["days"],                                    
                )
                payment.save()
                messages.success(
                    request,
                    f"Payment {data['code']} - {data['name']} creado exitosamente!",
                )
                return render(
                    request=request,
                    context={"payment_list": get_payments(request)},
                    template_name="payment/payment_list.html",
                )
            else:                
                messages.error(
                    request,
                    f"La condicion de pago {data['code']} - {data['name']} ya está creada",
                )

    payment_form = PaymentForm(request.POST)
    context_dict = {"form": payment_form}
    return render(
        request=request,
        context=context_dict,
        template_name="payment/payment_form.html",
    )


def payment_detail(request, pk: int):
    return render(
        request=request,
        context={"payment": Payment.objects.get(pk=pk)},
        template_name="payment/payment_detail.html",
    )


def payment_update(request, pk: int):
    payment = Payment.objects.get(pk=pk)

    if request.method == "POST":
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            data = payment_form.cleaned_data
            payment.code = data["code"]
            payment.name = data["name"]
            payment.days = data["days"]            
            payment.save()

            return render(
                request=request,
                context={"payment": payment},
                template_name="payment/payment_detail.html",
            )

    payment_form = PaymentForm(model_to_dict(payment))
    context_dict = {
        "payment": payment,
        "form": payment_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name="payment/payment_form.html",
    )


def payment_delete(request, pk: int):
    payment = Payment.objects.get(pk=pk)
    if request.method == "POST":
        payment.delete()

        payments = Payment.objects.all()
        context_dict = {"payment_list": payments}
        return render(
            request=request,
            context=context_dict,
            template_name="payment/payment_list.html",
        )

    context_dict = {
        "payment": payment,
    }
    return render(
        request=request,
        context=context_dict,
        template_name="payment/payment_confirm_delete.html",
    )


from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from payment.models import Payment


class PaymentListView(ListView):
    model = Payment
    paginate_by = 8


class PaymentDetailView(DetailView):
    model = Payment
    fields = ["code", "name", "days"]


class PaymentCreateView(CreateView):
    model = Payment
    success_url = reverse_lazy("payment:payment-list")

    form_class = PaymentForm
    # fields = ["code", "name", "days]

    def form_valid(self, form):
        """Filter to avoid duplicate payments"""
        data = form.cleaned_data
        actual_objects = Payment.objects.filter(
            code=data["code"], name=data["name"]
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"La condicion de pago {data['code']} - {data['name']} ya está creado",
            )
            form.add_error("name", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Condicion de pago {data['code']} - {data['name']} creado exitosamente!",
            )
            return super().form_valid(form)


class PaymentUpdateView(UpdateView):
    model = Payment
    fields = ["code", "name", "days"]

    def get_success_url(self):
        payment_id = self.kwargs["pk"]
        return reverse_lazy("payment:payment-detail", kwargs={"pk": payment_id})


class PaymentDeleteView(DeleteView):
    model = Payment
    success_url = reverse_lazy("payment:payment-list")