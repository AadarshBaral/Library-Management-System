# Generated by Django 4.1.4 on 2022-12-24 11:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_issued'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issued',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message='Invalid Number', regex='@"^\\d{10}$"')]),
        ),
    ]
