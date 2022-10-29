from django.urls import path

from credit import views

app_name = "credit"
urlpatterns = [
    path("credits", views.credits, name= "credit-list"),
    path("credit/add", views.create_credit, name="credit-add"),
]
