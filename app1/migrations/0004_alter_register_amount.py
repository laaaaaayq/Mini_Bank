# Generated by Django 4.2.4 on 2023-09-03 16:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_register_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='Amount',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1000)]),
        ),
    ]
