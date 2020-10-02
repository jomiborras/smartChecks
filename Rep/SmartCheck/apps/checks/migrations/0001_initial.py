# Generated by Django 3.1 on 2020-10-02 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('bankId', models.AutoField(primary_key=True, serialize=False)),
                ('bankName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cheque',
            fields=[
                ('nroCheque', models.BigIntegerField(primary_key=True, serialize=False, verbose_name='Número de cheque')),
                ('fechaEmision', models.DateField(verbose_name='Fecha de Emision')),
                ('fechaPago', models.DateField()),
                ('monto', models.BigIntegerField(verbose_name='Monto')),
                ('descripcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('nombreEstado', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tercero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emisor', models.CharField(max_length=100)),
                ('nroCheque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checks.cheque')),
            ],
        ),
        migrations.CreateModel(
            name='Propio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destinario', models.CharField(max_length=100)),
                ('nroCheque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checks.cheque')),
            ],
        ),
        migrations.CreateModel(
            name='CuentasCorriente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nroCuenta', models.CharField(max_length=100)),
                ('bankId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checks.banco')),
            ],
        ),
    ]
