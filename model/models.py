from django.db import models

# Create your models here.
class Customer(models.Model):
    customerID = models.AutoField(primary_key=True)
    customerName = models.CharField(max_length=100)
    mobileNumber  = models.IntegerField(unique=True, null=True)
    address = models.TextField()
    date_added = models.DateField(auto_now_add=True)
                                                                 
    def __str__(self):
        return f"{self.customerName}"

class Transaction(models.Model):
    transactionID = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    price = models.IntegerField(null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    
    