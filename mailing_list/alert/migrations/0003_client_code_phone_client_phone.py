# Generated by Django 4.0.1 on 2022-01-23 12:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0002_client_rename_message_mailing_message_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='code_phone',
            field=models.CharField(blank=True, max_length=5, validators=[django.core.validators.RegexValidator(message='Phone code wrong!', regex='^\\d{3,5}$')]),
        ),
        migrations.AddField(
            model_name='client',
            name='phone',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\7?1?\\d{9,15}$')]),
        ),
    ]
