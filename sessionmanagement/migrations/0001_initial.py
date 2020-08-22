# Generated by Django 3.1 on 2020-08-22 15:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionStatus',
            fields=[
                ('status_id', models.AutoField(primary_key=True, serialize=False)),
                ('status_name', models.CharField(default=None, max_length=100)),
                ('added_date', models.DateTimeField(default=datetime.datetime.now)),
                ('last_modified_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('session_id', models.AutoField(primary_key=True, serialize=False)),
                ('login_time', models.DateTimeField(default=datetime.datetime.now)),
                ('logout_time', models.DateTimeField(default=datetime.datetime.now)),
                ('session_key', models.CharField(default=None, max_length=100)),
                ('login_source', models.CharField(default='mobile', max_length=100)),
                ('login_type', models.CharField(default='native', max_length=100)),
                ('logout_type', models.CharField(default='current_session', max_length=100)),
                ('last_activity_time', models.DateTimeField(default=datetime.datetime.now)),
                ('added_date', models.DateTimeField(default=datetime.datetime.now)),
                ('last_modified_date', models.DateTimeField(default=datetime.datetime.now)),
                ('profile_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
                ('status_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='sessionmanagement.sessionstatus')),
            ],
        ),
    ]