from django.shortcuts import render,redirect
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
    return render(request, 'vikoba/login.html', context)

def welcome(request):

    context = {}
    return render(request, 'vikoba/welcome.html', context)  

def logout(request):

    context = {}
    return render(request, 'vikoba/logout.html', context)  