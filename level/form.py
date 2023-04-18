from django import forms
from .models import FormData
from django.core import validators

class Registration(forms.ModelForm):
    class Meta:
        model=FormData
        fields=['username','email','phone']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control form-group input-group w-50','placeholder':'Username'}),
            'email':forms.EmailInput(attrs={'class':'form-control form-group input-group w-50','placeholder':'Email'}),
            'phone':forms.TextInput(attrs={'class':'form-control form-group input-group w-50','placeholder':'Mobile number'})
        }
