from django.urls import path

from product import views

app_name = "product"
urlpatterns = [
    path("products", views.products, name= "product-list"),
    path("product/add", views.create_product, name="product-add"),
]