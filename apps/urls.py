from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="apps"),
    path('search', views.search, name='search'),
]