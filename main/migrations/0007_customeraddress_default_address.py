# Generated by Django 4.2.5 on 2023-09-29 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_customeraddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeraddress',
            name='default_address',
            field=models.BooleanField(default=False),
        ),
    ]