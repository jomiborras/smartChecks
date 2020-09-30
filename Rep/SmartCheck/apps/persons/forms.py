from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        labels = {'first_name': 'Nombre', 'last_name': 'Apellido', 'email': 'Email', 'password': 'Constraseña'}
        widgets = {
            'first_name': forms.TextInput(attrs={'type': 'text', 'class':'form-control col-6'}),
            'last_name': forms.TextInput(attrs={'type': 'text', 'class': 'form-control col-6'}),
            'email': forms.TextInput(attrs={'type': 'email', 'class': 'form-control col-6'}),
            'password': forms.TextInput(attrs={'type': 'password', 'class': 'form-control col-6'})        
        }