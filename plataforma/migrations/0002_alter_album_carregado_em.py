# Generated by Django 4.0.2 on 2022-02-14 14:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='carregado_em',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
