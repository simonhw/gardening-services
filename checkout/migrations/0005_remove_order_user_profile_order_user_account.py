# Generated by Django 4.2.7 on 2024-09-17 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_useraccount'),
        ('checkout', '0004_alter_order_eircode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user_profile',
        ),
        migrations.AddField(
            model_name='order',
            name='user_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='accounts.useraccount'),
        ),
    ]
