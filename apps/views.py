from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.core import serializers

from apps.models import App

def index(request):
    return render(request, "apps/index.html")

def search(request):
    group = request.user.groups.all()

    if request.user.is_staff:
        apps = App.objects.order_by('-add_date')
    else:
        apps = App.objects.filter(place=group[0])

    # Filter by Keyword
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = apps.filter(
                Q(description__icontains=keywords) | 
                Q(title__icontains=keywords) | 
                Q(place__icontains=keywords) | 
                Q(app_type__icontains=keywords) | 
                Q(api__icontains=keywords) |
                Q(last_editor__icontains=keywords) |
                Q(web_app_version__icontains=keywords))
    
    paginator = Paginator(queryset_list, 20)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    data = serializers.serialize('json', apps)

    context = {
        'apps': paged_listings,
        'data': data,
    }

    return render(request, "pages/index.html", context)