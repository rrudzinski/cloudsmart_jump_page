from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required

from apps.models import App


# @login_required(login_url='/cloudsmart-jump-page/accounts/login')
@login_required(login_url='/accounts/login')
def index(request):
    group = request.user.groups.all()
    if request.user.is_staff or request.user.is_superuser:
        apps = App.objects.order_by('-add_date')
        place = ""
    else:
        apps = App.objects.filter(place=group[0])
        place = group[0]

    distinct_types = App.objects.order_by('app_type').distinct('app_type')
    distinct_states = App.objects.order_by('state').distinct('state')
    distinct_place = App.objects.order_by('place').distinct('place')

    paginator = Paginator(apps, 20)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    data = serializers.serialize('json', apps)

    context = {
        'data': data,
        'apps': paged_listings,
        'distinct_types': distinct_types,
        'distinct_states': distinct_states,
        'distinct_place': distinct_place,
        'group': group,
        'place': place,
    }

    return render(request, 'pages/index.html', context)
