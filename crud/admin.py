from django.contrib import admin

# Register your models here.
from .models import User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id','amount', 'txn_type','txn_info','time','balance')