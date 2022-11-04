# Create your views here.
from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


from product.forms import ProductForm
from product.models import Product


def get_products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 3)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)
    #return products

def products(request):
    return render(
        request=request,
        context={"product_list": get_products(request)},
        template_name="product/product_list.html",
    )


def product_create(request):                    # reemplazo de create_product por product_create
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
            if not actual_objects:
                product = Product(
                    code=data["code"],
                    description=data["description"],
                    unit_sales=data["unit_sales"],                      
                )
                product.save()
                messages.success(
                    request,
                    f"Product {data['code']} - {data['description']} creado exitosamente!",
                )
                return render(
                    request=request,
                    context={"product_list": get_products(request)},
                    template_name="product/product_list.html",
                )
            else:                
                messages.error(
                    request,
                    f"El producto {data['code']} - {data['description']} ya está creado",
                )

    product_form = ProductForm(request.POST)
    context_dict = {"form": product_form}
    return render(
        request=request,
        context=context_dict,
        template_name="product/product_form.html",
    )


def product_detail(request, pk: int):
    return render(
        request=request,
        context={"product": Product.objects.get(pk=pk)},
        template_name="product/product_detail.html",
    )


def product_update(request, pk: int):
    product = Product.objects.get(pk=pk)

    if request.method == "POST":
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            data = product_form.cleaned_data
            product.code = data["code"]
            product.description = data["description"]
            product.unit_sales = data["unit_sales"]
            product.save()

            return render(
                request=request,
                context={"product": product},
                template_name="product/product_detail.html",
            )

    product_form = ProductForm(model_to_dict(product))
    context_dict = {
        "product": product,
        "form": product_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name="product/product_form.html",
    )


def product_delete(request, pk: int):
    product = Product.objects.get(pk=pk)
    if request.method == "POST":
        product.delete()

        products = Product.objects.all()
        context_dict = {"product_list": products}
        return render(
            request=request,
            context=context_dict,
            template_name="product/product_list.html",
        )

    context_dict = {
        "product": product,
    }
    return render(
        request=request,
        context=context_dict,
        template_name="product/product_confirm_delete.html",
    )


from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from product.models import Product


class ProductListView(ListView):
    model = Product
    paginate_by = 3


class ProductDetailView(DetailView):
    model = Product
    fields = ["code", "description", "unit_sales" ]


class ProductCreateView(CreateView):
    model = Product
    success_url = reverse_lazy("product:product-list")

    form_class = ProductForm
    

    def form_valid(self, form):
        """Filter to avoid duplicate products"""
        data = form.cleaned_data
        actual_objects = Product.objects.filter(
            code=data["code"], description=data["description"]
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"El producto {data['code']} - {data['description']} ya está creado",
            )
            form.add_error("description", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Producto {data['code']} - {data['description']} creado exitosamente!",
            )
            return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    fields = ["code", "description", "unit_sales"]

    def get_success_url(self):
        product_id = self.kwargs["pk"]
        return reverse_lazy("product:product-detail", kwargs={"pk": product_id})


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("product:product-list")


