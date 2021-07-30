from django.db import models

class Deposit(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(default=0, max_digits=19, decimal_places=2)

    def __str__(self):
        return self.name
