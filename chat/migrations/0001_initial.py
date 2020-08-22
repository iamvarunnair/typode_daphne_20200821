# Generated by Django 3.1 on 2020-08-22 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRequestStatus',
            fields=[
                ('status_id', models.AutoField(primary_key=True, serialize=False)),
                ('status_name', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ChatRequest',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False)),
                ('requester_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='requester_id', to='profiles.profile')),
                ('respondent_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='respondent_id', to='profiles.profile')),
                ('status', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='chat.chatrequeststatus')),
            ],
        ),
    ]
