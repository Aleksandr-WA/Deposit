# Generated by Django 5.1 on 2024-08-23 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposit_calculator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='calculated_value',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
