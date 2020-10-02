from django import forms
from .models import Banco, CuentasCorriente, Cheque

# from .urls import reverse

class BancoForm(forms.ModelForm):
    class Meta:
        model = Banco
        fields = ['bankName']
        labels = {'bankName': 'Nombre del Banco'}
        widgets = {'bankName': forms.TextInput(attrs={'type': 'text', 'class':'form-control col-6'})}

class CuentasCorrienteForm(forms.ModelForm):
    class Meta:
        model = CuentasCorriente
        fields = ['bankId', 'nroCuenta']
        labels = {'bankId': 'Banco', 'nroCuenta': 'Número de Cuenta'}
        widgets = {
            'bankId': forms.Select(attrs={'class':'form-control col-6'}),
            'nroCuenta': forms.TextInput(attrs={'class':'form-control col-6'})
            }

class ChequePropioForm(forms.ModelForm):
    class Meta:
        model = Cheque
        fields = [
            'nroCuenta',
            'nroCheque',
            'fechaEmision',
            'fechaPago',
            'monto',
            'nombreEstado',
            'descripcion'
            ]
        labels = {
            'nroCuenta': 'Número de Cuenta',
            'nroCheque': 'Número de Cheque',
            'fechaEmision': 'Fecha de Emisión',
            'fechaPago': 'Fecha de Pago',
            'monto': 'Monto',
            'nombreEstado': 'Estado',
            'descripcion': 'Comentarios'
            }
        widgets = {'nroCuenta': forms.Select(attrs={'class':'form-control col-6'}),
                   'nroCheque': forms.TextInput(attrs={'type': 'text', 'class':'form-control col-6'}),
                   'fechaEmision': forms.DateInput(attrs={'type': 'date', 'class':'form-control col-6'}),
                   'fechaPago': forms.DateInput(attrs={'type': 'date', 'class':'form-control col-6'}),
                   'monto': forms.NumberInput(attrs={'type': 'number', 'class':'form-control col-6'}),
                   'nombreEstado': forms.Select(attrs={'class':'form-control col-6'}),
                   'descripcion': forms.Textarea(attrs={'class':'form-control col-6', 'rows': '6'})
                   }