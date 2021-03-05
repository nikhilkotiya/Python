from django.contrib import admin
from django.urls import path
from . import views #importing all function and class from views.py file

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="index"),#views.index is a funcation name which we are write in viwes.py file
]