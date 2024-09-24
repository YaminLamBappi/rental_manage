# Generated by Django 5.1.1 on 2024-09-24 08:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental_management', '0009_rentcollection_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='flat_number',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='rental_management.unit'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='flat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='units', to='rental_management.flat'),
        ),
        migrations.AlterField(
            model_name='unit',
            name='status',
            field=models.CharField(choices=[('occupied', 'Occupied'), ('vacant', 'Vacant')], default='vacant', max_length=20),
        ),
        migrations.AlterUniqueTogether(
            name='unit',
            unique_together={('flat', 'name')},
        ),
    ]
