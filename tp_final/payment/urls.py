from django.urls import path

from payment import views

app_name = "payment"
urlpatterns = [
    path("payments", views.payments, name= "payment-list"),
    path("payment/add", views.create_payment, name="payment-add"),
]