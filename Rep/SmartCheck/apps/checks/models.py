from django.db import models
from apps.persons.models import *
from django.conf import settings

# Create your models here.

class Banco(models.Model):
    bankId = models.AutoField(primary_key=True)
    bankName = models.CharField(max_length=100)
    def __str__(self):
        return self.bankName

class CuentasCorriente(models.Model):
    nroCuenta = models.CharField(max_length=100)
    bankId = models.ForeignKey(Banco, on_delete=models.CASCADE)
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    # email = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.bankId

    def __str__(self):
        return self.nroCuenta

    # def __str__(self):
    #     return self.userId

class Estado(models.Model):
    nombreEstado = models.CharField(max_length = 100,primary_key=True)

    def __str__(self):
        return self.nombreEstado

class Cheque(models.Model):
    nroCuenta = models.ForeignKey(CuentasCorriente, on_delete=models.CASCADE)
    nroCheque = models.BigIntegerField(verbose_name="Número de cheque", primary_key=True)
    fechaEmision = models.DateField(auto_now = False ,auto_now_add = False,verbose_name="Fecha de Emision")
    fechaPago = models.DateField(auto_now = False ,auto_now_add = False)
    monto = models.BigIntegerField(verbose_name="Monto")
    nombreEstado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=255)

    def __str__(self):
        return self.nroCuenta

    def __str__(self):
        return self.nombreEstado

class Propio(models.Model):
	nroCheque = models.ForeignKey(Cheque, on_delete=models.CASCADE)
	destinario = models.CharField(max_length = 100)

class Tercero(models.Model):
	nroCheque = models.ForeignKey(Cheque, on_delete=models.CASCADE)
	emisor = models.CharField(max_length = 100)