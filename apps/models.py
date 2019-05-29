from django.db import models
from datetime import datetime

APP_TYPES = (
    ('Local Govt', 'Local Govt'),
    ('Story', 'Story'),
    ('Template', 'Template'),
    ('WAB Editor', 'WAB Editor'),
    ('WAB Other', 'WAB Other'),
    ('WAB Viewer', 'WAB Viewer'),
)

API_VERSIONS = (
    ('3.0', '3.0'),
    ('3.1', '3.1'),
    ('3.2', '3.2'),
    ('3.3', '3.3'),
    ('3.4', '3.4'),
    ('3.5', '3.5'),
    ('3.6', '3.6'),
    ('3.7', '3.7'),
    ('3.8', '3.8'),
    ('3.9', '3.9'),
    ('3.10', '3.10'),
    ('3.11', '3.11'),
    ('3.12', '3.12'),
    ('3.13', '3.13'),
    ('3.14', '3.14'),
    ('3.15', '3.15'),
    ('3.16', '3.16'),
    ('3.17', '3.17'),
    ('3.18', '3.18'),
    ('3.19', '3.19'),
    ('3.21', '3.21'),
    ('3.22', '3.22'),
    ('3.23', '3.23'),
    ('3.24', '3.24'),
    ('3.27', '3.27'),
    ('3.28', '3.28'),
    ('4.0', '4.0'),
    ('4.1', '4.1'),
    ('4.2', '4.2'),
    ('4.3', '4.3'),
    ('4.4', '4.4'),
    ('4.5', '4.5'),
    ('4.6', '4.6'),
    ('4.7', '4.7'),
    ('4.8', '4.8'),
    ('4.9', '4.9'),
    ('4.10', '4.10'),
    ('4.11', '4.11'),
)

WEBAPP_VERSION = (
    ('N/A', 'N/A'),
    ('1.0', '1.0'),
    ('1.1', '1.1'),
    ('1.2', '1.2'),
    ('1.3', '1.3'),
    ('1.4', '1.4'),
    ('2.0', '2.0'),
    ('2.0.1', '2.0.1'),
    ('2.1', '2.1'),
    ('2.2', '2.2'),
    ('2.3', '2.3'),
    ('2.4', '2.4'),
    ('2.5', '2.5'),
    ('2.6', '2.6'),
    ('2.7', '2.7'),
    ('2.8', '2.8'),
    ('2.9', '2.9'),
    ('2.10', '2.10'),
    ('2.11', '2.11'),
    ('2.12', '2.12'),
)

CATEGORIES = (
    ('Accessibility Services', 'Accessibility Services'),
    ('Administrative Services', 'Administrative Services'),
    ('ArcGIS Online Services', 'ArcGIS Online Services'),
    ('Cemetery Services', 'Cemetery Services'),
    ('Data Collection Services', 'Data Collection Services'),
    ('Easement Services', 'Easement Services'),
    ('Economic Development Services', 'Economic Development Services'),
    ('Environmental Services', 'Environmental Services'),
    ('Event Services', 'Event Services'),
    ('General Services', 'General Services'),
    ('Mining Services', 'Mining Services'),
    ('Parcel/Addressing Services', 'Parcel/Addressing Services'),
    ('Recreational Services', 'Recreational Services'),
    ('SEI Administration', 'SEI Administration'),
    ('Transportation Services', 'Transportation Services'),
    ('Utility System Services', 'Utility System Services'),
    ('Water Right Services', 'Water Right Services'),
    ('Zoning Services', 'Zoning Services'),

)
SORTED_CATEGORIES = sorted(CATEGORIES, key=lambda x: x[1])

EDITORS = (
    ('Benjamin Cserepes', 'Benjamin Cserepes'),
    ('Benjamin Smith', 'Benjamin Smith'),
    ('Christopher Daughton', 'Christopher Daughton'),
    ('Jarom Hlebasko', 'Jarom Hlebasko'),
    ('John McLaughlin', 'John McLaughlin'),
    ('Rafal Rudzinski', 'Rafal Rudzinski'),
    ('Unknown','Unknown'),
)
SORTED_EDITORS = sorted(EDITORS, key=lambda x: x[1])

PLACES = (
    ('Afton WY', 'Afton WY'),
    ('Ashley Valley (UT) Water & Sewer District (AVWSID)', 'Ashley Valley (UT) Water & Sewer District (AVWSID)'),
    ('Bedford (WY) Water & Sewer District (BWSD)', 'Bedford (WY)  Water & Sewer District (BWSD)'),
    ('Big Park (AZ) Domestic Wastewater Improvement District (DWWID)', 'Big Park (AZ) Domestic Wastewater Improvement District (DWWID)'),
    ('Big Water UT', 'Big Water UT'),
    ('Caliente NV', 'Caliente NV'),
    ('Cedar Highlands UT', 'Cedar Highlands UT'),
    ('Centerfield UT', 'Centerfield UT'),
    ('Cochise County AZ', 'Cochise County AZ'),
    ('Clark County NV', 'Clark County NV'),
    ('Delta UT', 'Delta UT'),
    ('Demonstration (Demo)', 'Demonstration (Demo)'),
    ('Dixie Deer (UT) Special Service District (SSD)', 'Dixie Deer (UT) Special Service District (SSD)'),
    ('Enoch UT', 'Enoch UT'),
    ('Fillmore UT', 'Fillmore UT'),
    ('Gila County AZ', 'Gila County AZ'),
    ('Greenlee County AZ', 'Greenlee County AZ'),
    ('Gunnison UT', 'Gunnison UT'),
    ('Hildale UT', 'Hildale UT'),
    ('Ivins UT', 'Ivins UT'),
    ('Johnson Water Improvement District (UT) (JWID)', 'Johnson Water Improvement District (UT) (JWID)'),
    ('Kane County (UT) Water Conservancy District (KCWCD)', 'Kane County (UT) Water Conservancy District (KCWCD)'),
    ('LaVerkin UT', 'LaVerkin UT'),
    ('Lincoln County NV', 'Lincoln County NV'),
    ('Milford UT', 'Milford UT'),
    ('Manila UT', 'Manila UT'),
    ('Maricopa County AZ', 'Maricopa County AZ'),
    ('Mayfield UT', 'Mayfield UT'),
    ('Minden NV', 'Minden NV'),
    ('Moapa Valley (NV) Water System (MVWD)', 'Moapa Valley (NV) Water System (MVWD)'),
    ('Mt. Pleasant UT', 'Mt. Pleasant UT'),
    ('Neola UT', 'Neola UT'),
    ('Parowan UT', 'Parowan UT'),
    ('Payson AZ Area', 'Payson AZ Area'),
    ('Pima County AZ', 'Pima County AZ'),
    ('Pinal County AZ', 'Pinal County AZ'),
    ('Pine Bluffs WY', 'Pine Bluffs WY'),
    ('Rockville UT', 'Rockville UT'),
    ('Santa Clara UT', 'Santa Clara UT'),
    ('Southwest (UT) Mosquito Abatement Control District (SWMACD)', 'Southwest (UT) Mosquito Abatement Control District (SWMACD)'),
    ('Springdale UT', 'Springdale UT'),
    ('St George UT', 'St George UT'),
    ('Summit UT', 'Summit UT'),
    ('Sunrise Engineering, Inc.', 'Sunrise Engineering, Inc.'),
    ('Thanksgiving Point UT', 'Thanksgiving Point UT'),
    ('Tridell Lapoint UT', 'Tridell Lapoint UT'),
    ('Tropic UT', 'Tropic UT'),
    ('Uintah County UT', 'Uintah County UT'),
    ('Vernal UT', 'Vernal UT'),
    ('Washington City UT', 'Washington City UT'),
    ('Washington County UT', 'Washington County UT'),
    ('Yuma County AZ', 'Yuma County AZ'),
)
SORTED_PLACES = sorted(PLACES, key=lambda x: x[1])

STATES = (
    ('AZ', 'AZ'),
    ('CA', 'CA'),
    ('CO', 'CO'),
    ('ID', 'ID'),
    ('NM', 'NM'),
    ('NV', 'NV'),
    ('OR', 'OR'),
    ('SEI', 'SEI'),
    ('UT', 'UT'),
    ('WA', 'WA'),
    ('WY', 'WY'),
)
SORTED_STATES = sorted(STATES, key=lambda x: x[1])

class App(models.Model):
    add_date         = models.DateTimeField(auto_now_add=True)
    api              = models.CharField("API Version", max_length=10, choices=API_VERSIONS, blank=True)
    app_type         = models.CharField(max_length=20, choices=APP_TYPES)
    category         = models.CharField(max_length=100, choices=SORTED_CATEGORIES)
    description      = models.TextField()
    is_demo          = models.BooleanField(default=False)
    last_edited      = models.DateTimeField("Last Edited", default=datetime.now, blank=True)
    last_editor      = models.CharField("Last Editor", max_length=100, choices=SORTED_EDITORS)
    photo            = models.ImageField(upload_to='photos/', blank=True)
    place            = models.CharField(max_length=100, choices=SORTED_PLACES, blank=True)
    state            = models.CharField(max_length=10, choices=SORTED_STATES)
    title            = models.CharField(max_length=100)
    url              = models.CharField(max_length=200)
    web_app_version  = models.CharField(max_length=20, choices=WEBAPP_VERSION, blank=True)

def __str__(self):
    return self.title