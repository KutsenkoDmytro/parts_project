# Generated by Django 3.2.19 on 2024-03-30 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_axial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cross_number',
            field=models.TextField(blank=True, db_index=True, default='', verbose_name='cross number'),
        ),
    ]