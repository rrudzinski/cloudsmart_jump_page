# Generated by Django 2.0.9 on 2018-12-04 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_auto_20181204_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='url',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
    ]
