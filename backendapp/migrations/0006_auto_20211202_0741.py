# Generated by Django 3.2.4 on 2021-12-02 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0005_remove_subscriptions_no_of_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='foreign_subscriptions',
        ),
        migrations.AlterField(
            model_name='subscriptions',
            name='image',
            field=models.TextField(default=''),
        ),
    ]
