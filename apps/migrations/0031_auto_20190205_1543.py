# Generated by Django 2.0.9 on 2019-02-05 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0030_auto_20181218_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='api',
            field=models.CharField(blank=True, choices=[('3.26', '3.26'), ('4.9', '4.9')], max_length=10, verbose_name='API Version'),
        ),
        migrations.AlterField(
            model_name='app',
            name='category',
            field=models.CharField(choices=[('Accessibility Services', 'Accessibility Services'), ('Administrative Services', 'Administrative Services'), ('ArcGIS Online Services', 'ArcGIS Online Services'), ('Cemetery Services', 'Cemetery Services'), ('Data Collection Services', 'Data Collection Services'), ('Easement Services', 'Easement Services'), ('Economic Development Services', 'Economic Development Services'), ('Event Services', 'Event Services'), ('General Services', 'General Services'), ('Mining Services', 'Mining Services'), ('Parcel/Addressing Services', 'Parcel/Addressing Services'), ('Recreational Services', 'Recreational Services'), ('Transportation Services', 'Transportation Services'), ('Utility System Services', 'Utility System Services'), ('Water Right Services', 'Water Right Services'), ('Zoning Services', 'Zoning Services')], max_length=100),
        ),
        migrations.AlterField(
            model_name='app',
            name='last_editor',
            field=models.CharField(choices=[('Benjamin Cserepes', 'Benjamin Cserepes'), ('Benjamin Smith', 'Benjamin Smith'), ('Christopher Daughton', 'Christopher Daughton'), ('Jarom Hlebasko', 'Jarom Hlebasko'), ('John McLaughlin', 'John McLaughlin'), ('Rafal Rudzinski', 'Rafal Rudzinski')], max_length=100, verbose_name='Last Editor'),
        ),
        migrations.AlterField(
            model_name='app',
            name='web_app_version',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
