from django import forms
from .models import Compra

class CompraForm(forms.ModelForm): 
        # cliente = forms.CharField(widget=forms.TextInput(attrs={'':'','class': 'form-control btn-block',}))
        # produto= forms.Select(widget=forms.TextInput(attrs={'class': 'form-control',}))

        class Meta:
                model=Compra
                fields = [
                'cliente',
                'produto',
                'quantidade'
        ]
