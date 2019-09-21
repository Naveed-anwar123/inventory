from django.db import models
from datetime import datetime
# Create your models here.
class IronStoreTransaction(models.Model):
    receipt_id = models.CharField(max_length=100,primary_key=True)
    total_amount = models.CharField(max_length=100)
    firt_time_paid = models.CharField(max_length=100,default=0)
    advance = models.CharField(max_length=100,default=0)
    first_time_damount = models.CharField(default=0,max_length=100)
    discount = models.CharField(default=0,max_length=100)
    notes = models.TextField()
    cname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    added_at = models.DateTimeField()
    today_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.receipt_id



class IronStoreTransactionItems(models.Model):
    receipt = models.ForeignKey(IronStoreTransaction, on_delete=models.CASCADE)
    item_id = models.IntegerField()
    item_name = models.CharField(max_length=100)
    item_quantity = models.CharField(max_length=100)
    item_unit_price = models.CharField(max_length=100)
    item_total_price = models.CharField(default=0,max_length=100)
    added_at = models.DateTimeField()
    def __str__(self):
        return self.receipt_id

    @property
    def total_cost(self):
        return self.item_quantity * self.item_unit_price


class IronStoreTransactionHistory(models.Model):
    receipt = models.ForeignKey(IronStoreTransaction, on_delete=models.CASCADE)
    paid = models.CharField(max_length=100)
    advance = models.CharField(max_length=100,default=0)
    damount = models.CharField(default=0,max_length=100)
    added_at = models.DateTimeField()
    today_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.receipt_id        


class IronStoreDailyExpenses(models.Model):
    description = models.CharField(max_length=100)
    amount = models.CharField(max_length=100,default=0)
    today_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.description