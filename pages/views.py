from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# # First lesson test the http
# def index(request):
#     return HttpResponse("<h1>Hello, World!</h1>")

def index(request):
    
    return render(request,'pages/index.html')
#print(request.path) ## for print request object information to console

def about(request):
    
    return render(request,'pages/about.html')