from django.contrib import admin
from .models import Customer, Transaction
# Register your models here.
for i in [Customer, Transaction]:
    admin.site.register(i)