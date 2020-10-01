from django.shortcuts import render, redirect
from django.urls import reverse

# from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()

# from .forms import RegisterUserForm, LoginForm

from django.urls import reverse_lazy

from django.views.generic.edit import FormView

from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseRedirect, HttpResponse

from django.contrib import messages

from . import forms

# ------------------------------------------------------
# from apps.checks import urls
# from .models import User

# from django.contrib.auth import authenticate
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import login as do_login

# from django.contrib.auth.forms import UserCreationForm
# from .forms import UserForm

# from django.contrib.auth import logout as do_logout
# ------------------------------------------------------

# Create your views here.

# ------------------------------------------------------
# def login(request):

# 	# Creamos el formulario de autenticación vacío
# 	form = LoginForm()
# 	if request.method == "POST":
# 		# Añadimos los datos recibidos al formulario
# 		form = LoginForm(data=request.POST)
# 		# Si el formulario es válido...
# 		if form.is_valid():
# 			# Recuperamos las credenciales validadas
# 			email = form.cleaned_data['email']
# 			password = form.cleaned_data['password']

# 			# Verificamos las credenciales del usuario
# 			user = authenticate(email=email, password=password)

# 			# Si existe un usuario con ese nombre y contraseña
# 			if user is not None:
# 				# Hacemos el login manualmente
# 				do_login(request, user)
# 				# Y le redireccionamos a la portada
# 				return redirect('main')

# 	# Si llegamos al final renderizamos el formulario
# 	return render(request, "login.html", {'form': form})
# 	# return render(request, 'login.html', {})
# ------------------------------------------------------
# def logon(request):
# 	# Creamos el formulario de autenticación vacío
# 	form = UserCreationForm()
# 	if request.method == "POST":
# 		# Añadimos los datos recibidos al formulario
# 		form = UserCreationForm(data=request.POST)
# 		# Si el formulario es válido...
# 		if form.is_valid():
# 			# Creamos la nueva cuenta de usuario
# 			user = form.save()

# 			#  Si el usuario se crea correctamente
# 			if user is not None:
# 				# Hacemos el login manualmente
# 				do_login(request, user)
# 				# Y le redireccionamos a la portada
# 				return redirect('main')
	
# 	form.fields['username'].help_text = None
# 	form.fields['password1'].help_text = None
# 	form.fields['password2'].help_text = None
# 	# Si llegamos al final, renderizamos el formulario
# 	return render(request, "logon.html", {'form': form})
# 	# return render(request, 'logon.html', {})
# ------------------------------------------------------
# def logout(request):
# 	do_logout(request)
# 	return render(request, 'home.html', {})
# ------------------------------------------------------
# def login(request):

# 	form = LoginForm()
# 	if request.method == "POST":


# 	template_name = 'main.html'
# 	success_url = reverse_lazy('main.html')
	

# 	return render(request, 'login.html', {'form': form})

# class LoginView(FormView):
# 	"""login view"""

# 	form_class = forms.LoginForm
# 	success_url = reverse_lazy('main')
# 	template_name = 'login'

# 	def form_valid(self, form):
# 		""" process user login"""
# 		credentials = form.cleaned_data

# 		user = authenticate(
# 			username=credentials['email'],
# 			password=credentials['password']
# 			)

# 		if user is not None:
# 			login(self.request, user)
# 			return HttpResponseRedirect(self.success_url)

# 		else:
# 			messages.add_message(self.request, messages.INFO, 'Mail y/o Contraseña inválidos\
# 				Intente nuevamente, si el problema persiste, use otro sistema')
# 			return HttpResponseRedirect(reverse_lazy('login'))
# ------------------------------------------------------
class LoginView(FormView):
	form = LoginForm()
	form_class = form.LoginForm()
	template_name = 'login.html'

	def form_valid(self, form):
		email = form.cleaned_data['email']
		password = form.cleaned_data['password']
		user = authenticate(email=email, password=password)

		# Check here if the user is an admin
		if user is not None and user.is_active:
			login(self.request, user)
			return HttpResponseRedirect(self.success_url)
		else:
			return self.form_invalid(form)

def logon(request):

	form = RegisterUserForm()
	if request.method == "POST":
		form = RegisterUserForm(data=request.POST)

		if form.is_valid():
			user = form.save()

			if user is not None:
				do_login(request, user)
				return redirect('main')

	return render(request, 'logon.html', {'form': form})

def logout(request):
	do_logout(request)
	return render(request, 'home.html', {})