# Generated by Django 4.1.2 on 2022-11-11 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_pedidos'),
    ]

    operations = [
        migrations.CreateModel(
            name='TiposDePizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=50)),
                ('ingredientes', models.CharField(max_length=150)),
                ('descripcion', models.CharField(max_length=150)),
                ('codigo_producto', models.IntegerField()),
            ],
        ),
    ]
