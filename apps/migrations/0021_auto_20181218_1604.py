# Generated by Django 2.0.9 on 2018-12-19 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0020_auto_20181204_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='place',
            field=models.CharField(choices=[('Afton', 'Afton'), ('Big Park', 'Big Park'), ('Caliente', 'Caliente'), ('Clark County', 'Clark County'), ('Lincoln County', 'Lincoln County'), ('MVWD', 'MVWD'), ('Minden', 'Minden'), ('Pima County', 'Pima County'), ('Pine Bluffs', 'Pine Bluffs')], max_length=100),
        ),
    ]
