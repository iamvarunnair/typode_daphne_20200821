# Generated by Django 3.1 on 2020-08-24 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sessionmanagement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='session',
            old_name='status_id',
            new_name='status',
        ),
    ]