from django.core import validators
from django import forms
from .models import User

class UserDetails(forms.ModelForm):
    class Meta:
        model=User
        fields=['user_id','amount', 'txn_type','txn_info','balance']