from base.models import User
from django.shortcuts import render
from .forms import UserRegister

# Create your views here.

def addAndshow(req):
    if req.method == "POST":
        ur = UserRegister(req.POST)
        ur.save()       
    else:
        ur = UserRegister()
        
    return render(req,"addAndshow.html",{"form":ur})