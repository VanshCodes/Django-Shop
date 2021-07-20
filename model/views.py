from django.http.response import HttpResponse
from model.serializers import CustomerSerializer
from .models import Customer
from rest_framework import generics


class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


def r(request):
    return HttpResponse("GET")
