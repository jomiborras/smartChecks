from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Banco)
class BancoAdmin(admin.ModelAdmin):
    list_display = ['bankId', 'bankName']

@admin.register(CuentasCorriente)
class CuentasCorrienteAdmin(admin.ModelAdmin):
    list_display = ['nroCuenta', 'bankId', 'email']

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ['nombreEstado']

@admin.register(Cheque)
class ChaqueAdmin(admin.ModelAdmin):
    list_display = ['numeroCuenta', 'nroCheque', 'fechaEmision', 'fechaPago', 'monto', 'nombreEstado']

@admin.register(Propio)
class PropioAdmin(admin.ModelAdmin):
    list_display = ['nroCheque', 'destinario']

@admin.register(Tercero)
class TerceroAdmin(admin.ModelAdmin):
    list_display = ['nroCheque', 'emisor']
