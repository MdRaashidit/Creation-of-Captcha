from .forms import *
from django.contrib import messages
from django.shortcuts import render

def home(request):
    
    if request.method=="POST":
        form=raashid(request.POST)
        if form.is_valid():
            messages.success(request,'Sucesss !!')
        else:
            messages.error(request,'Wrong captcha !!')
    form=raashid()
    return render(request,'home.html',{'form':form})
 