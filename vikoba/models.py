from django.db import models
from django.contrib.auth.models import User

class Deposit(models.Model):
    depositer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=19, decimal_places=2)

    def __str__(self):
        return self.name
