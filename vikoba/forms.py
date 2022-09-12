from django.forms import ModelForm
from .models import Deposit

class DepositForm(ModelForm):
    class Meta:
        model = Deposit
        # widgets = {
        #     'name': form.name(attrs={'class': 'form-control','placeholder':'name'}),
        #     'amount': form.amount(attrs={'class': 'form-control','placeholder':'amount deposit'}),
        # }
        # fields = '__all__'
        fields = ('amount',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['amount'].widget.attrs.update({'class':'form-control', 'placeholder':'amount deposit'})     

