from django.db import models
from datetime import datetime

APP_TYPES = (
    ('Editor', 'Editor'),
    ('Viewer', 'Viewer'),
)

API_VERSIONS = (
    ('3.16', '3.16'),
    ('3.17', '3.17'),
    ('3.18', '3.18'),
    ('3.19', '3.19'),
    ('3.21', '3.21'),
    ('3.22', '3.22'),
    ('3.23', '3.23'),
    ('3.24', '3.24'),
    ('3.27', '3.27'),
)

WEBAPP_VERSION = (
    ('1.3', '1.3'),
    ('1.4', '1.4'),
    ('2.1', '2.1'),
    ('2.2', '2.2'),
    ('2.3', '2.3'),
    ('2.5', '2.5'),
    ('2.6', '2.6'),
    ('2.7', '2.7'),
    ('2.8', '2.8'),
    ('2.11', '2.11'),
)

CATEGORIES = (
    ('Accessibility Services', 'Accessibility Services'),
    ('Administrative Services', 'Administrative Services'),
    ('ArcGIS Online Services', 'ArcGIS Online Services'),
    ('Cemetery Services', 'Cemetery Services'),
    ('Data Collection Services', 'Data Collection Services'),
    ('Easement Services', 'Easement Services'),
    ('Economic Development Services', 'Economic Development Services'),
    ('Event Services', 'Event Services'),
    ('General Services', 'General Services'),
    ('Mining Services', 'Mining Services'),
    ('Parcel/Addressing Services', 'Parcel/Addressing Services'),
    ('Recreational Services', 'Recreational Services'),
    ('Transportation Services', 'Transportation Services'),
    ('Utility System Services', 'Utility System Services'),
    ('Water Right Services', 'Water Right Services'),
    ('Zoning Services', 'Zoning Services'),

)
SORTED_CATEGORIES = sorted(CATEGORIES, key=lambda x: x[1])

EDITORS = (
    ('Rafal Rudzinski', 'Rafal Rudzinski'),
    ('Benjamin Cserepes', 'Benjamin Cserepes'),
    ('Jarom Hlebasko', 'Jarom Hlebasko'),
    ('Christopher Daughton', 'Christopher Daughton'),
    ('John McLaughlin', 'John McLaughlin'),
    ('Benjamin Smith', 'Benjamin Smith'),
)
SORTED_EDITORS = sorted(EDITORS, key=lambda x: x[1])

PLACES = (
    ('Big Park', 'Big Park'),
    ('Pima County', 'Pima County'),
    ('Lincoln County', 'Lincoln County'),
    ('Minden', 'Minden'),
    ('MVWD', 'MVWD'),
    ('Afton', 'Afton'),
    ('Caliente', 'Caliente'),
    ('Clark County', 'Clark County'),
    ('Pine Bluffs', 'Pine Bluffs'),
    ('Demo', 'Demo'),
    ('Centerfield', 'Centerfield'),
    ('Enoch', 'Enoch'),
    ('Ashley Vally (AVWSID)', 'Ashley Vally (AVWSID)'),
    ('Big Water', 'Big Water'),
    ('BWSD (WY)', 'BWSD (WY)'),
    ('Cedar Highlands', 'Cedar Highlands'),
    ('Delta', 'Delta'),
    ('Fillmore', 'Fillmore'),
    ('Gunnison', 'Gunnison'),
    ('Ivins', 'Ivins'),
    ('Hildale', 'Hildale'),
    ('JWID', 'JWID'),
    ('Kane County (KCWCD)', 'Kane County (KCWCD)'),
    ('LaVerkin', 'LaVerkin'),
    ('Manila', 'Manila'),
    ('Mayfield', 'Mayfield'),
    ('Neola', 'Neola'),
    ('Parowan', 'Parowan'),
    ('Rockville', 'Rockville'),
    ('Santa Clara', 'Santa Clara'),
    ('Springdale', 'Springdale'),
    ('St George', 'St George'),
    ('SWMACD', 'SWMACD'),
    ('Summit', 'Summit'),
    ('Thanksgiving Point', 'Thanksgiving Point'),
    ('Tridell Lapoint', 'Tridell Lapoint'),
    ('Tropic', 'Tropic'),
    ('Uintah', 'Uintah'),
    ('Vernal', 'Vernal'),
    ('Washington', 'Washington'),

)
SORTED_PLACES = sorted(PLACES, key=lambda x: x[1])

STATES = (
    ('AZ', 'AZ'),
    ('NV', 'NV'),
    ('SEI', 'SEI'),
    ('UT', 'UT'),
    ('WY', 'WY')
)
SORTED_STATES = sorted(STATES, key=lambda x: x[1])

class App(models.Model):
    title = models.CharField(max_length=100)
    place = models.CharField(max_length=100, choices=SORTED_PLACES, blank=True)
    state = models.CharField(max_length=10, choices=SORTED_STATES)
    category = models.CharField(max_length=100, choices=SORTED_CATEGORIES)
    description = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/', blank=True)
    api = models.CharField("API Version", max_length=10, choices=API_VERSIONS, blank=True)
    app_type = models.CharField(max_length=20, choices=APP_TYPES)
    web_app_version = models.CharField(max_length=20, choices=WEBAPP_VERSION, blank=True)
    last_editor = models.CharField("Last Editor", max_length=100, choices=SORTED_EDITORS)
    last_edited = models.DateTimeField("Last Edited", default=datetime.now, blank=True)
    is_demo = models.BooleanField(default=False)
    url = models.CharField(max_length=200)

def __str__(self):
    return self.title