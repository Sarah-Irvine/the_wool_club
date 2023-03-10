from django.shortcuts import render, get_object_or_404
from .models import Workshop 
from datetime import datetime

def details(request, id):
    workshop = get_object_or_404(Workshop, id=id)
    print(workshop)
    return render(request, 'learn/details.html', {'workshop': workshop})


def list(request):
    today = datetime.today()

    filter_map = {
        'keywords': 'keywords__icontains',
    }

    filters = {}
    for key, value in request.GET.items():
        filter_key = filter_map[key]
        filters[filter_key] = value


    workshops = Workshop.objects.filter(
          #Greater than or equal to
          datetime__gte=today).filter(**filters).order_by('datetime')
 
    return render(request, 'learn/list.html', {'workshops': workshops})


def learn(request):
    return render(request, 'learn/learn.html')

def stitch_guide(request):
    return render(request, 'learn/stitch_guide.html')

def the_basics(request):
    return render(request, 'learn/the_basics.html')


