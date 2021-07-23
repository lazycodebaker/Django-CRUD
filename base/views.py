
from django.http.response import HttpResponseRedirect
from base.models import User
from django.shortcuts import render
from .forms import UserRegister

# Create your views here.

def addAndshow(req):
    if req.method == "POST":
        ur = UserRegister(req.POST)
        ur.save()       
        ur = UserRegister()
    else:
        ur = UserRegister()
    
    users = User.objects.all()
        
    return render(req,"addAndshow.html",{"form":ur,"users":users})


def delteUser(req,id):
    if req.method == "POST":
        usr = User.objects.get(pk=id)
        usr.delete()
        return HttpResponseRedirect('/')      

def updateUserInfo(req,id):
    if req.method == "POST":
        user = User.objects.get(pk=id)
        ur = UserRegister(req.POST,instance=user)
        ur.save()
    else:
        user = User.objects.get(pk=id)
        ur = UserRegister(instance=user)        
    return render(req,'update.html',{"form":ur})

