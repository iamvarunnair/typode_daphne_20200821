# Generated by Django 3.1 on 2020-08-22 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TokenStatus',
            fields=[
                ('status_id', models.AutoField(primary_key=True, serialize=False)),
                ('status_name', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TokenType',
            fields=[
                ('type_id', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ApiTokens',
            fields=[
                ('token_id', models.AutoField(primary_key=True, serialize=False)),
                ('token_string', models.CharField(default='', max_length=100)),
                ('status', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='apiauthentication.tokenstatus')),
                ('token_type', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='apiauthentication.tokentype')),
            ],
        ),
    ]