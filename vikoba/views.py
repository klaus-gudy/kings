from django.shortcuts import render,redirect
from .models import *
from .forms import DepositForm

from django.views.generic import ListView, TemplateView, CreateView

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

class DisplayView(TemplateView):
    template_name = "vikoba/welcome.html"

class DisplayDeposit(LoginRequiredMixin, ListView):
    model = Deposit
    template_name = "vikoba/display.html"
    context_object_name = 'deposit'

class DepositView(LoginRequiredMixin, CreateView):
    form_class = DepositForm
    template_name = "vikoba/deposit.html"
    success_url =reverse_lazy('display')

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super(DepositView, self).form_valid(form)

class IndividualDeposit(LoginRequiredMixin, ListView):
    model = Deposit
    template_name = "vikoba/mydeposit.html"
    context_object_name = 'deposit'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['deposit'] = context['deposit'].filter(name=self.request.user)
        return context

