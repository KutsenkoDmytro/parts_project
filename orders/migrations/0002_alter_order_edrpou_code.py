# Generated by Django 3.2.19 on 2023-07-01 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='edrpou_code',
            field=models.IntegerField(verbose_name='edrpou code'),
        ),
    ]