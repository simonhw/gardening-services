# Generated by Django 4.2.7 on 2024-09-20 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_alter_review_created_on_alter_review_updated_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='updated_on',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
