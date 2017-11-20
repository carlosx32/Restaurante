from orden.forms import OrdenForms
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.
def index(request):
    return render(request,'orden/index.html')
    #return HttpResponse("Menu")
def nueva(request):
    if (request.method=='POST'):
        form= OrdenForms(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'orden/exito.html')
    else:
            form=OrdenForms()
            return render(request,'orden/nuevaorden.html',{'form':form})
