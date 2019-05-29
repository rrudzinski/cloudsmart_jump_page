# Generated by Django 2.0.9 on 2019-02-06 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0032_auto_20190205_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='place',
            field=models.CharField(choices=[('Afton', 'Afton'), ('Ashley Vally (AVWSID)', 'Ashley Vally (AVWSID)'), ('BWSD (WY)', 'BWSD (WY)'), ('Big Park', 'Big Park'), ('Big Water', 'Big Water'), ('Caliente', 'Caliente'), ('Cedar Highlands', 'Cedar Highlands'), ('Centerfield', 'Centerfield'), ('Clark County', 'Clark County'), ('Delta', 'Delta'), ('Demo', 'Demo'), ('Enoch', 'Enoch'), ('Fillmore', 'Fillmore'), ('Gunnison', 'Gunnison'), ('Hildale', 'Hildale'), ('Ivins', 'Ivins'), ('JWID', 'JWID'), ('Kane County (KCWCD)', 'Kane County (KCWCD)'), ('LaVerkin', 'LaVerkin'), ('Lincoln County', 'Lincoln County'), ('MVWD', 'MVWD'), ('Manila', 'Manila'), ('Mayfield', 'Mayfield'), ('Minden', 'Minden'), ('Neola', 'Neola'), ('Parowan', 'Parowan'), ('Pima County', 'Pima County'), ('Pine Bluffs', 'Pine Bluffs'), ('Rockville', 'Rockville'), ('SWMACD', 'SWMACD'), ('Santa Clara', 'Santa Clara'), ('Springdale', 'Springdale'), ('St George', 'St George'), ('Summit', 'Summit'), ('Thanksgiving Point', 'Thanksgiving Point'), ('Tridell Lapoint', 'Tridell Lapoint'), ('Tropic', 'Tropic'), ('Uintah', 'Uintah'), ('Vernal', 'Vernal'), ('Washington', 'Washington')], max_length=100),
        ),
    ]
