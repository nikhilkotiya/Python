from django.shortcuts import render # render is used to connect html file seprately , so we can esily write html code
from .models import User
from .forms import UserDetails
# Create your views here.
def index(request):
    if request.method=="POST":
        fm = UserDetails(request.POST)
        if fm.is_valid():
            fm.save()
            fm = UserDetails()
    else:
        fm = UserDetails()
    return render(request,"index.html",{'form':fm})