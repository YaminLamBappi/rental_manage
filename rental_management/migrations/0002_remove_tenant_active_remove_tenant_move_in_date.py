# Generated by Django 5.1.1 on 2024-09-23 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental_management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenant',
            name='active',
        ),
        migrations.RemoveField(
            model_name='tenant',
            name='move_in_date',
        ),
    ]
