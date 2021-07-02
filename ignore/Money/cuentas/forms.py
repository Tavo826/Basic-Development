from django import forms
from django.forms import widgets
from .models import Cuenta


class CuentaForm(forms.ModelForm):

    class Meta:
        model = Cuenta
        fields = ('tipo', 'cantidad', 'categoria', 'descripcion')
        widgets = {
            'tipo': forms.RadioSelect(),
            # 'categoria': forms.Select(attrs={'class': 'form-control col-sm-2'})
            'categoria': forms.CheckboxSelectMultiple()
        }
