from django import forms
from .models import Cliente


class ClienteForm(forms.Form):
    class Meta:
        
        nome = forms.CharField(required=True)
        terminal = forms.IntegerField(required=False)
        morada = forms.CharField(required=False)
    
