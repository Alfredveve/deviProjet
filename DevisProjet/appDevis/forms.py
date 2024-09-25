# forms.py
from django import forms
from .models import Devis, Service

class DevisForm(forms.ModelForm):

    class Meta:
        model = Devis
        fields = ['service', 'pays', 'ville', 'commune', 'quartier', 'nom_client', 'email', 'tel_whatsapp', 'numero_devis']
        widgets = {
            'service': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Service'}),
            'pays': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Pays'}),
            'ville': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ville'}),
            'commune': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Commune'}),
            'quartier': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Quartier'}),
            'nom_client': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom Client'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'tel_whatsapp': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telephon Whatsapp'}),
            'numero_devis': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numero Devis'}),
        }


class ServiceForm(forms.ModelForm):
    class Meta: 
        model = Service
        fields = ['id', 'nom', 'description', 'prix_unitaire']
      