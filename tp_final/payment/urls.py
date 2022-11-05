from django.urls import path

from payment import views

app_name = "payment"
urlpatterns = [
    #path("payments", views.payments, name= "payment-list"),
    #path("payment/add", views.create_payment, name="payment-add"),
    
    path("payments/", views.PaymentListView.as_view(), name="payment-list"),
    path("payment/add/", views.PaymentCreateView.as_view(), name="payment-add"),
    path("payment/<int:pk>/detail/", views.PaymentDetailView.as_view(), name="payment-detail"),
    path("payment/<int:pk>/update/", views.PaymentUpdateView.as_view(), name="payment-update"),
    path("payment/<int:pk>/delete/", views.PaymentDeleteView.as_view(), name="payment-delete"),
]