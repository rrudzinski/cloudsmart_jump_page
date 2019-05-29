from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cloudsmart-jump-page/', include('pages.urls')),
    path('cloudsmart-jump-page/apps', include('apps.urls')),
    path('cloudsmart-jump-page/accounts/', include('accounts.urls')),
    path('cloudsmart-jump-page/admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
