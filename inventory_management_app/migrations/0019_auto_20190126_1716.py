# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-01-26 17:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_management_app', '0018_auto_20190122_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
        migrations.AlterField(
            model_name='box',
            name='Location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory_management_app.Location'),
        ),
        migrations.AlterField(
            model_name='box',
            name='project_assigned_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory_management_app.Project'),
        ),
        migrations.AlterField(
            model_name='historicalbox',
            name='Location',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='inventory_management_app.Location'),
        ),
        migrations.AlterField(
            model_name='historicalbox',
            name='project_assigned_to',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='inventory_management_app.Project'),
        ),
        migrations.AlterField(
            model_name='historicalproject',
            name='project_manager',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
