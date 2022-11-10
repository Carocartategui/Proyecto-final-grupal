# Generated by Django 4.1.2 on 2022-11-10 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('numero_documento', models.IntegerField()),
                ('numero_de_telefono', models.IntegerField()),
                ('e_mail', models.CharField(max_length=100)),
                ('contrasena', models.CharField(max_length=100)),
            ],
        ),
    ]
