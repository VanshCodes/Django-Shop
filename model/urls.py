from model.views import CustomerDetail, CustomerList
from django.urls import path

urlpatterns = [
    path("customers/", CustomerList.as_view(), name="customer.details"),
    path("customer/<int:pk>", CustomerDetail.as_view(), name="customer.details"),

]
