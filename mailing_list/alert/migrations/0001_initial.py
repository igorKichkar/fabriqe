# Generated by Django 4.0.1 on 2022-01-21 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=11)),
                ('code_phone', models.CharField(max_length=10)),
                ('tag', models.CharField(max_length=100)),
                ('time_zone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mailing_start', models.DateTimeField()),
                ('message', models.TextField()),
                ('filter_client', models.CharField(max_length=100)),
                ('mailing_end', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_creation', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=50, null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='alert.customer')),
                ('mailing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mailig_complete', to='alert.mailing')),
            ],
        ),
    ]
