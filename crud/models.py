from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField()
    amount = models.PositiveIntegerField() 
    balance = models.PositiveIntegerField()
    txn_type= models.CharField(max_length=60)
    txn_info = models.CharField(max_length=60)
    time = models.DateTimeField(auto_now_add=True, blank=True)