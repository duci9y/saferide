# Generated by Django 2.2.7 on 2019-11-19 05:33

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='end_loc',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='ride',
            name='start_loc',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='user',
            name='abuse_lock',
            field=models.BooleanField(default=False),
        ),
    ]
