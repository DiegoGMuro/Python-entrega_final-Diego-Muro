from django.urls import path

from home import views

app_name = "home"
urlpatterns = [
    path("", views.index, name="index"),
    path("searchc/", views.searchc, name="searchc"),
    path("searchp/", views.searchp, name="searchp"),
]
