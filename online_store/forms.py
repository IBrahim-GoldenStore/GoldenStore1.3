from django import forms
from .models import *


class commands(forms.ModelForm):
    color= forms.ModelChoiceField(queryset= Color.objects.all(),label="Couleurs",required=False)
    class Meta:
        model= Commande
        fields= ['number','adresse','color',]
        label= {
            'number': 'Numero', 
            'adresse': 'Adresse',
            'color': 'Couleur',
        }
    

class Panier_form(forms.ModelForm):
    type= forms.CharField(max_length= 10,widget= forms.HiddenInput, label='Type', initial="Panier",disabled= True)

    class Meta:
        model= Commande
        fields= ['number','adresse','e_mail',]
