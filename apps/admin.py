from django.contrib import admin

from .models import App

class AppAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'place', 'state', 'app_type', 'api',)
    list_display_links = ('id', 'title',)
    list_filter = ('state',)
    search_fields = ('title', 'place', 'state', 'description', 'app_type', 'api',)
    list_per_page = 25

admin.site.register(App, AppAdmin)
