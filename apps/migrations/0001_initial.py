# Generated by Django 2.0.9 on 2018-11-26 22:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Date')),
                ('photo', models.ImageField(upload_to='photos/')),
                ('api', models.CharField(blank=True, max_length=100, verbose_name='API Version')),
                ('app_type', models.CharField(choices=[('editor', 'Editor'), ('viewer', 'Viewer')], default='viewer', max_length=20)),
                ('is_demo', models.BooleanField(default=False)),
            ],
        ),
    ]
