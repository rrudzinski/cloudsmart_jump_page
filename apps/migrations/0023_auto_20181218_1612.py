# Generated by Django 2.0.9 on 2018-12-19 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0022_auto_20181218_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='category',
            field=models.CharField(choices=[('Capacity Customers', 'Capacity Customers'), ('Pavement Management', 'Pavement Management'), ('Permits', 'Permits'), ('Power System', 'Power System'), ('Road System', 'Road System'), ('Sewer System', 'Sewer System'), ('Tax Parcel', 'Tax Parcel'), ('Utility Systems', 'Utility Systems'), ('Water System', 'Water System'), ('Zoning', 'Zoning')], max_length=100),
        ),
    ]
