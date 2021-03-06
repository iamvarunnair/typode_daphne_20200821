# Generated by Django 3.1 on 2020-08-25 11:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatrequest',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='chatrequest',
            name='last_modified_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='chatrequeststatus',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='chatrequeststatus',
            name='last_modified_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
