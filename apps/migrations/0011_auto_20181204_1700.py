# Generated by Django 2.0.9 on 2018-12-05 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0010_auto_20181204_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='app_type',
            field=models.CharField(choices=[('editor', 'Editor'), ('viewer', 'Viewer')], max_length=20),
        ),
    ]