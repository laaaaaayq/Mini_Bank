# Generated by Django 4.2.4 on 2023-09-05 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_login_acc_number_alter_register_acc_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='Amount',
            field=models.IntegerField(),
        ),
    ]
