from django.urls import path

from credit import views

app_name = "credit"
urlpatterns = [
    #path("credits", views.credits, name= "credit-list"),
    #path("credit/add", views.create_credit, name="credit-add"),
    
    path("credits/", views.CreditListView.as_view(), name="credit-list"),
    path("credit/add/", views.CreditCreateView.as_view(), name="credit-add"),
    path("credit/<int:pk>/detail/", views.CreditDetailView.as_view(), name="credit-detail"),
    path("credit/<int:pk>/update/", views.CreditUpdateView.as_view(), name="credit-update"),
    path("credit/<int:pk>/delete/", views.CreditDeleteView.as_view(), name="credit-delete"),
]
