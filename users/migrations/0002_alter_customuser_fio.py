# Generated by Django 4.1.2 on 2022-12-22 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='fio',
            field=models.CharField(default='', max_length=270, verbose_name='ФИО'),
        ),
    ]
