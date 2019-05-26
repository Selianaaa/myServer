# Generated by Django 2.2.1 on 2019-05-23 21:08

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('image_vector', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), null=True, size=None)),
            ],
            options={
                'db_table': 'items',
            },
        ),
    ]
