# Generated by Django 2.0.9 on 2019-05-22 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0042_auto_20190520_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='category',
            field=models.CharField(choices=[('Accessibility Services', 'Accessibility Services'), ('Administrative Services', 'Administrative Services'), ('ArcGIS Online Services', 'ArcGIS Online Services'), ('Cemetery Services', 'Cemetery Services'), ('Data Collection Services', 'Data Collection Services'), ('Easement Services', 'Easement Services'), ('Economic Development Services', 'Economic Development Services'), ('Environmental Services', 'Environmental Services'), ('Event Services', 'Event Services'), ('General Services', 'General Services'), ('Mining Services', 'Mining Services'), ('Parcel/Addressing Services', 'Parcel/Addressing Services'), ('Recreational Services', 'Recreational Services'), ('SEI Administration', 'SEI Administration'), ('Transportation Services', 'Transportation Services'), ('Utility System Services', 'Utility System Services'), ('Water Right Services', 'Water Right Services'), ('Zoning Services', 'Zoning Services')], max_length=100),
        ),
    ]
