import django_tables2 as tables
from apps.models import App

class AppTable(tables.Table):
    class Meta:
        model = App
        template_name = 'django_tables2/bootstrap-responsive.html'