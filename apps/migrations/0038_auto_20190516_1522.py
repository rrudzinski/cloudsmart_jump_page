# Generated by Django 2.0.9 on 2019-05-16 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0037_auto_20190516_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='app_type',
            field=models.CharField(choices=[('Local Govt', 'Local Govt'), ('Story', 'Story'), ('Template', 'Template'), ('WAB Editor', 'WAB Editor'), ('WAB Other', 'WAB Other'), ('WAB Viewer', 'WAB Viewer')], max_length=20),
        ),
    ]
