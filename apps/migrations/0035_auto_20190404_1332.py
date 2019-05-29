# Generated by Django 2.0.9 on 2019-04-04 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0034_auto_20190205_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='api',
            field=models.CharField(blank=True, choices=[('3.16', '3.16'), ('3.17', '3.17'), ('3.18', '3.18'), ('3.19', '3.19'), ('3.21', '3.21'), ('3.22', '3.22'), ('3.23', '3.23'), ('3.24', '3.24'), ('3.27', '3.27')], max_length=10, verbose_name='API Version'),
        ),
        migrations.AlterField(
            model_name='app',
            name='web_app_version',
            field=models.CharField(blank=True, choices=[('1.3', '1.3'), ('1.4', '1.4'), ('2.1', '2.1'), ('2.2', '2.2'), ('2.3', '2.3'), ('2.5', '2.5'), ('2.6', '2.6'), ('2.7', '2.7'), ('2.8', '2.8'), ('2.11', '2.11')], max_length=20),
        ),
    ]