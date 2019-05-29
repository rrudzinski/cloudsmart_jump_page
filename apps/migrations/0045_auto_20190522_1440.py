# Generated by Django 2.0.9 on 2019-05-22 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0044_auto_20190522_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='place',
            field=models.CharField(blank=True, choices=[('Afton WY', 'Afton WY'), ('Ashley Valley (UT) Water & Sewer District (AVWSID)', 'Ashley Valley (UT) Water & Sewer District (AVWSID)'), ('Bedford (WY) Water & Sewer District (BWSD)', 'Bedford (WY)  Water & Sewer District (BWSD)'), ('Big Park (AZ) Domestic Wastewater Improvement District (DWWID)', 'Big Park (AZ) Domestic Wastewater Improvement District (DWWID)'), ('Big Water UT', 'Big Water UT'), ('Caliente NV', 'Caliente NV'), ('Cedar Highlands UT', 'Cedar Highlands UT'), ('Centerfield UT', 'Centerfield UT'), ('Clark County NV', 'Clark County NV'), ('Cochise County AZ', 'Cochise County AZ'), ('Delta UT', 'Delta UT'), ('Demonstration (Demo)', 'Demonstration (Demo)'), ('Enoch UT', 'Enoch UT'), ('Fillmore UT', 'Fillmore UT'), ('Gila County AZ', 'Gila County AZ'), ('Greenlee County AZ', 'Greenlee County AZ'), ('Gunnison UT', 'Gunnison UT'), ('Hildale UT', 'Hildale UT'), ('Ivins UT', 'Ivins UT'), ('Johnson Water Improvement District (UT) (JWID)', 'Johnson Water Improvement District (UT) (JWID)'), ('Kane County (UT) Water Conservancy District (KCWCD)', 'Kane County (UT) Water Conservancy District (KCWCD)'), ('LaVerkin UT', 'LaVerkin UT'), ('Lincoln County NV', 'Lincoln County NV'), ('Manila UT', 'Manila UT'), ('Maricopa County AZ', 'Maricopa County AZ'), ('Mayfield UT', 'Mayfield UT'), ('Milford UT', 'Milford UT'), ('Minden NV', 'Minden NV'), ('Moapa Valley (NV) Water System (MVWD)', 'Moapa Valley (NV) Water System (MVWD)'), ('Mt. Pleasant UT', 'Mt. Pleasant UT'), ('Neola UT', 'Neola UT'), ('Parowan UT', 'Parowan UT'), ('Payson AZ Area', 'Payson AZ Area'), ('Pima County AZ', 'Pima County AZ'), ('Pinal County AZ', 'Pinal County AZ'), ('Pine Bluffs WY', 'Pine Bluffs WY'), ('Rockville UT', 'Rockville UT'), ('Santa Clara UT', 'Santa Clara UT'), ('Southwest (UT) Mosquito Abatement Control District (SWMACD)', 'Southwest (UT) Mosquito Abatement Control District (SWMACD)'), ('Springdale UT', 'Springdale UT'), ('St George UT', 'St George UT'), ('Summit UT', 'Summit UT'), ('Sunrise Engineering, Inc.', 'Sunrise Engineering, Inc.'), ('Thanksgiving Point UT', 'Thanksgiving Point UT'), ('Tridell Lapoint UT', 'Tridell Lapoint UT'), ('Tropic UT', 'Tropic UT'), ('Uintah County UT', 'Uintah County UT'), ('Vernal UT', 'Vernal UT'), ('Washington City UT', 'Washington City UT'), ('Washington County UT', 'Washington County UT'), ('Yuma County AZ', 'Yuma County AZ')], max_length=100),
        ),
    ]