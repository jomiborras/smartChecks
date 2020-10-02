# # from django import forms
# # from django.contrib.auth import get_user_model
# # # from django.contrib.auth.models import User
# # # from .models import User

# # # class UserForm(forms.ModelForm):

# # #     first_name = forms.CharField(max_length=100)
# # #     last_name = forms.CharField(max_length=100)
# # #     email = forms.EmailField(max_length=255)
# # #     password = forms.PasswordInput()
    
# # #     class Meta:
# # #         model = User
# # #         fields = ['first_name', 'last_name', 'email', 'password']
# # #         labels = {'first_name': 'Nombre', 'last_name': 'Apellido', 'email': 'Email', 'password': 'Constraseña'}
# # #         widgets = {
# # #             'first_name': forms.TextInput(attrs={'type': 'text', 'class':'form-control col-6'}),
# # #             'last_name': forms.TextInput(attrs={'type': 'text', 'class': 'form-control col-6'}),
# # #             'email': forms.TextInput(attrs={'type': 'email', 'class': 'form-control col-6'}),
# # #             'password': forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control col-6'})        
# #         # }

# # class RegisterUserForm(forms.ModelForm):
# #     class Meta:
# #         model = get_user_model()
# #         fields = ['first_name', 'last_name', 'email', 'password']
# #         labels = {
# #             'first_name': 'Nombre',
# #             'last_name': 'Apellido',
# #             'email': 'Email',
# #             'password': 'Contraseña'
# #             }
# #         widgets = {
# #             'first_name': forms.TextInput(attrs={'type': 'text', 'class':'form-control col-6'}),
# #             'last_name': forms.TextInput(attrs={'type': 'text', 'class': 'form-control col-6'}),
# #             'email': forms.TextInput(attrs={'type': 'email', 'class': 'form-control col-6'}),
# #             'password': forms.TextInput(attrs={'type': 'password', 'class': 'form-control col-6'})
# #         }

# # class LoginForm(forms.Form):
# #     """User Login Form"""
# #     email = forms.EmailField()
# #     password = forms.CharField(widget=forms.PasswordInput())

# from django import forms
# from .models import Banco, CuentasCorriente, Cheque

# # from .urls import reverse

# class BancoForm(forms.ModelForm):
#     class Meta:
#         model = Banco
#         fields = ['bankName']
#         labels = {'bankName': 'Nombre del Banco'}
#         widgets = {'bankName': forms.TextInput(attrs={'type': 'text', 'class':'form-control col-6'})}

# class CuentasCorrienteForm(forms.ModelForm):
#     class Meta:
#         model = CuentasCorriente
#         fields = ['bankId', 'nroCuenta']
#         labels = {'bankId': 'Banco', 'nroCuenta': 'Número de Cuenta'}
#         bankName = forms.ModelChoiceField(queryset=Banco.objects.all(), required=True)
#         widgets = {
#             'bankId': forms.Select(attrs={'class':'form-control col-6'}),
#             'nroCuenta': forms.TextInput(attrs={'class':'form-control col-6'})
#             }

# class ChequePropioForm(forms.ModelForm):
#     class Meta:
#         model = Cheque
#         fields = ['numeroCuenta', 'nroCheque', 'fechaEmision', 'fechaPago', 'monto', 'nombreEstado', 'descripcion']
#         labels = {'numeroCuenta': 'Número de Cuenta', 'nroCheque': 'Número de Cheque', 'fechaEmision': 'Fecha de Emisión', 'fechaPago': 'Fecha de Pago', 'monto': 'Monto', 'nombreEstado': 'Estado', 'descripcion': 'Comentarios'}
#         # widgets = {'numeroCuenta': forms.Select(attrs={'class':'form-control col-6'}),
#         #            'nroCheque': forms.TextInput(attrs={'type': 'text', 'class':'form-control col-6'}),
#         #            'fechaEmision': forms.DateField(attrs={'type': 'text', 'class':'form-control col-6'}),
#         #            'fechaPago': forms.DateField(attrs={'type': 'text', 'class':'form-control col-6'}),
#         #            'monto': forms.DecimalField(attrs={'type': 'number', 'class':'form-control col-6'}, required=False),
#         #            'nombreEstado': forms.Select(attrs={'class':'form-control col-6'}),
#         #            'descripcion': forms.Textarea(attrs={'class':'form-control col-6', 'rows': '6'})
#         #            }

from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']