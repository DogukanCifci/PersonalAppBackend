# Generated by Django 4.1.5 on 2023-01-16 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_personal_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='ended',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
