# Generated by Django 2.0.9 on 2018-12-05 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0019_auto_20181204_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='app_type',
            field=models.CharField(choices=[('Editor', 'Editor'), ('Viewer', 'Viewer')], max_length=20),
        ),
        migrations.AlterField(
            model_name='app',
            name='category',
            field=models.CharField(choices=[('Pavement Management', 'Pavement Management'), ('Power System', 'Power System'), ('Road System', 'Road System'), ('Sewer System', 'Sewer System'), ('Tax Parcel', 'Tax Parcel'), ('Utility Systems', 'Utility Systems'), ('Water System', 'Water System'), ('Zoning', 'Zoning')], max_length=100),
        ),
        migrations.AlterField(
            model_name='app',
            name='last_editor',
            field=models.CharField(choices=[('Benjamin Cserepes', 'Benjamin Cserepes'), ('Christopher Daughton', 'Christopher Daughton'), ('Jarom Hlebasko', 'Jarom Hlebasko'), ('John McLaughlin', 'John McLaughlin'), ('Rafal Rudzinski', 'Rafal Rudzinski')], max_length=100, verbose_name='Last Editor'),
        ),
        migrations.AlterField(
            model_name='app',
            name='place',
            field=models.CharField(choices=[('Afton', 'Afton'), ('BPDWWID', 'BPDWWID'), ('Caliente', 'Caliente'), ('Clark County', 'Clark County'), ('Lincoln County', 'Lincoln County'), ('MVWD', 'MVWD'), ('Minden', 'Minden'), ('Pima County', 'Pima County'), ('Pine Bluffs', 'Pine Bluffs')], max_length=100),
        ),
    ]
