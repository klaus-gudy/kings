from django.shortcuts import render
from .models import *

# def base(request):
#     context = {}
#     return render(request, 'vikoba/base.html', context)

def deposit(request):
    deposits = Deposit.objects.order_by('-date')

    context = {'deposits':deposits}
    return render(request, 'vikoba/deposit.html', context)

def display(request):
    context = {}
    return render(request, 'vikoba/display.html', context)