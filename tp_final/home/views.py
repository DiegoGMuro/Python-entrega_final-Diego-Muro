from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.forms.models import model_to_dict
from django.shortcuts import redirect
from django.shortcuts import render

from django.core.paginator import Paginator
# Create your views here.
from customer.models import Customer
from home.forms import UserRegisterForm
from home.forms import UserUpdateForm

from product.models import Product
from payment.models import Payment
from credit.models import Credit

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

def register(request):
    form = UserRegisterForm(request.POST) if request.POST else UserRegisterForm()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado exitosamente!")
            return redirect("login")

    return render(
        request=request,
        context={"form": form},
        template_name="registration/register.html",
    )


@login_required
def user_update(request):
    user = request.user
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("home:index")

    form = UserUpdateForm(model_to_dict(user))
    return render(
        request=request,
        context={"form": form},
        template_name="registration/user_form.html",
    )
    
    