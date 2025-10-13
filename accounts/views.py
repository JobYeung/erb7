from django.shortcuts import render, redirect
from django.contrib import messages

def register(request):
    if request.method == "POST":
        print("submit")
        messages.success(request,"Account created successfully")
        # storage = messages.get_messages(request)
        # for message in storage:
        #     print(message.level_tag,message.message)
        return redirect('accounts:register')
    else:
        return render(request,'accounts/register.html')

def login(request):
    return render(request,'accounts/login.html')

def logout(request):
    return redirect("pages:index")

def dashboard(request):
    return render(request,'accounts/dashboard.html')
