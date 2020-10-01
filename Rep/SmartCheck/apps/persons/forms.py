from django import forms
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User
# from .models import User

# class UserForm(forms.ModelForm):

#     first_name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)
#     email = forms.EmailField(max_length=255)
#     password = forms.PasswordInput()
    
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'password']
#         labels = {'first_name': 'Nombre', 'last_name': 'Apellido', 'email': 'Email', 'password': 'Constraseña'}
#         widgets = {
#             'first_name': forms.TextInput(attrs={'type': 'text', 'class':'form-control col-6'}),
#             'last_name': forms.TextInput(attrs={'type': 'text', 'class': 'form-control col-6'}),
#             'email': forms.TextInput(attrs={'type': 'email', 'class': 'form-control col-6'}),
#             'password': forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control col-6'})        
        # }

class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'password']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Email',
            'password': 'Contraseña'
            }
        widgets = {
            'first_name': forms.TextInput(attrs={'type': 'text', 'class':'form-control col-6'}),
            'last_name': forms.TextInput(attrs={'type': 'text', 'class': 'form-control col-6'}),
            'email': forms.TextInput(attrs={'type': 'email', 'class': 'form-control col-6'}),
            'password': forms.TextInput(attrs={'type': 'password', 'class': 'form-control col-6'})
        }

class LoginForm(forms.Form):
    """User Login Form"""
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())