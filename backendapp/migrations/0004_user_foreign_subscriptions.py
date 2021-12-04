# Generated by Django 3.2.4 on 2021-12-02 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0003_remove_user_subscriptions'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='foreign_subscriptions',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='backendapp.subscriptions'),
        ),
    ]
