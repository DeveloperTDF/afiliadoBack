# Generated by Django 3.2.10 on 2024-10-04 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afiliados', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='afiliado',
            name='direccion',
            field=models.CharField(max_length=30),
        ),
    ]
