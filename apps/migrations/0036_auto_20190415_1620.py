# Generated by Django 2.0.9 on 2019-04-15 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0035_auto_20190404_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/'),
        ),
    ]