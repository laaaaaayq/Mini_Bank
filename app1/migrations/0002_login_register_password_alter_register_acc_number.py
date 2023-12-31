# Generated by Django 4.2.4 on 2023-09-03 08:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Acc_number', models.IntegerField(unique='true')),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='register',
            name='Password',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='register',
            name='Acc_number',
            field=models.IntegerField(unique='true'),
        ),
    ]
