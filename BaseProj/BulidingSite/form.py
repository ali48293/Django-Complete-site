from django import forms
from .models import addDev

class devForm(forms.ModelForm):
    
    class Meta:
        """Meta definition for MODELNAMEform."""

        model = addDev
        fields = '__all__'
