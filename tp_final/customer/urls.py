from django.urls import path

from customer import views

app_name = "customer"
urlpatterns = [
    path("customers", views.customers, name= "customer-list"),
    path("customer/add", views.create_customer, name="customer-add"),
]