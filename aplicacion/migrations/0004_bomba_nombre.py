# Generated by Django 4.2.4 on 2023-12-10 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_rename_litroscargados_bomba_litrosactuales'),
    ]

    operations = [
        migrations.AddField(
            model_name='bomba',
            name='nombre',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]