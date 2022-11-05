from django.urls import path

from customer import views

app_name = "customer"
urlpatterns = [
    # path("customers", views.customers, name= "customer-list"),
    # path("customer/add", views.create_customer, name="customer-add"),
    
    path("customers/", views.CustomerListView.as_view(), name="customer-list"),
    path("customer/add/", views.CustomerCreateView.as_view(), name="customer-add"),
    path("customer/<int:pk>/detail/", views.CustomerDetailView.as_view(), name="customer-detail"),
    path("customer/<int:pk>/update/", views.CustomerUpdateView.as_view(), name="customer-update"),
    path("customer/<int:pk>/delete/", views.CustomerDeleteView.as_view(), name="customer-delete"),
    path("comment/<int:pk>/add/", views.CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment-delete"),
]