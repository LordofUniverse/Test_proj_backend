# Generated by Django 3.2.4 on 2021-12-03 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0010_subscriptions_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptions',
            name='price',
            field=models.TextField(default='500'),
        ),
    ]
