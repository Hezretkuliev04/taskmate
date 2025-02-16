from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomRegisterForm
from django.contrib import messages
# Create your views here.

def debug_logout(request):
    return HttpResponse(f"Method used: {request.method}")


def registration(request):
    if request.method == "POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request , ("New account started to log in!"))
            return redirect('registration') #redireçt  пиши name = " "  c Urls  а не название register.html 
    else:        
        register_form = CustomRegisterForm()
    return render(request , 'register.html' , {'register_form': register_form} ) # в render используй хтмл страницу