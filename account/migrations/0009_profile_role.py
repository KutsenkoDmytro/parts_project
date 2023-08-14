# Generated by Django 3.2.19 on 2023-08-01 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_userrole_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='profiles_user_role', to='account.userrole', verbose_name='role'),
        ),
    ]