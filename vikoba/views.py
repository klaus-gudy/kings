from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm 
# from django.contrib import messages
from .models import *
from .forms import DepositForm

# def base(request):
#     context = {}
#     return render(request, 'vikoba/base.html', context)

def deposit(request):
    deposits = Deposit.objects.order_by('-date')

    context = {'deposits':deposits}
    return render(request, 'vikoba/deposit.html', context)

def display(request):
    form = DepositForm()
    if request.method == 'POST':
        form = DepositForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('deposit')
    else:
        form = DepositForm()

    context = {'form' : form}
    return render(request, 'vikoba/display.html', context)

def login(request):

    context = {}
    return render(request, 'auth/login.html', context)



def welcome(request):

    context = {}
    return render(request, 'auth/welcome.html', context)  

def logout(request):

    context = {}
    return render(request, 'auth/logout.html', context)  

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()    

    context = {'form': form}
    return render(request, 'auth/register.html', context)    

# def register(request):

#     context = {}
#     if request.method == "POST":
#         context = {'has_error': False}
#         email = request.POST.get('email')
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         password2 = request.POST.get('password2')

#         if password != password2:
#             messages.add_message(request, messages.ERROR, 'password didnt match')

#             context['has_error'] = True

#         if context['has_error']:
#             return render(request, 'auth/register.html')

#         user.set_password(password)
#         user.save()

#         messages.add_message(request, messages.SUCCESS, 'you can now login')   

    
#     return render(request, 'auth/register.html', context)    