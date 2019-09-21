from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_type = models.CharField(max_length=100)
    item_subtype = models.CharField(max_length=30)
    item_price = models.IntegerField()
    item_code = models.CharField(max_length=30)
    item_quantity = models.CharField(max_length=30)
    item_description = models.TextField()
    added_at = models.DateTimeField()
    

    def __str__(self):
        return self.item_name