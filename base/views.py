from django.shortcuts import render

# Create your views here.

def addAndshow(req):
    return render(req,"addAndshow.html")