
from django.http.response import HttpResponseRedirect
from base.models import User
from django.shortcuts import render
from .forms import UserRegister

# Create your views here.


def delteUser(req,id):
    if req.method == "POST":
        usr = User.objects.get(pk=id)
        usr.delete()
        return HttpResponseRedirect('/')      


def addAndshow(req):
    if req.method == "POST":
        ur = UserRegister(req.POST)
        ur.save()       
        ur = UserRegister()
    else:
        ur = UserRegister()
    
    users = User.objects.all()
        
    return render(req,"addAndshow.html",{"form":ur,"users":users})