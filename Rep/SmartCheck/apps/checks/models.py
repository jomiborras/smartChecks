from django.db import models
from apps.persons.models import *

# Create your models here.

class Banco(models.Model):
    bankId = models.AutoField(primary_key=True)
    bankName = models.CharField(max_length=100)

class CuentasCorriente(models.Model):
    nroCuenta = models.CharField(max_length=100)
    bankId = models.ForeignKey(Banco, on_delete=models.CASCADE)
    email = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.bankName

class Estado(models.Model):
	nombreEstado = models.CharField(max_length = 100,primary_key=True)

class Cheque(models.Model):
    numeroCuenta = models.ForeignKey(CuentasCorriente, on_delete=models.CASCADE)
    nroCheque = models.BigIntegerField(verbose_name="Número de cheque", primary_key=True)
    fechaEmision = models.DateField(auto_now = False ,auto_now_add = False,verbose_name="Fecha de Emision")
    fechaPago = models.DateField(auto_now = False ,auto_now_add = False)
    monto = models.BigIntegerField(verbose_name="Monto")
    nombreEstado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)

class Propio(models.Model):
	nroCheque = models.ForeignKey(Cheque, on_delete=models.CASCADE)
	destinario = models.CharField(max_length = 100)

class Tercero(models.Model):
	nroCheque = models.ForeignKey(Cheque, on_delete=models.CASCADE)
	emisor = models.CharField(max_length = 100)