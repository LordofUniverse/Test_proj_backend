# Generated by Django 3.2.4 on 2021-12-02 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0006_auto_20211202_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='subs',
            field=models.TextField(default=''),
        ),
    ]
