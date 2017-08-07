from django.shortcuts import render,HttpResponse

# Create your views here.

def add(request):
    return render(request,'add.html')