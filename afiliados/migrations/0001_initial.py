# Generated by Django 3.2.10 on 2024-10-03 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Afiliado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('nombre', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=10)),
            ],
        ),
    ]
