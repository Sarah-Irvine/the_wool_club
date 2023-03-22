from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Workshop, Stitch, BasicArticle
from datetime import datetime
from accounts.models import UserProfile


def check_if_user_profile(request):
    if request.user.is_authenticated:
        [profile, created] = UserProfile.objects.get_or_create(
            user=request.user)
        return profile

# add/remove attendance at workshops
   
@login_required
def add_attending(request, id):
    workshop = get_object_or_404(Workshop, id=id)
    if request.method == "POST":
        request.user.profile.attending.add(workshop)
    return redirect(request.POST.get("redirect_url"))


@login_required
def remove_attending(request, id):
    workshop = get_object_or_404(Workshop, id=id)
    if request.method == "POST":
        request.user.profile.attending.remove(workshop)
    return redirect(request.POST.get("redirect_url"))


@login_required
def my_workshops(request):
    today = datetime.today()
    profile = check_if_user_profile(request)

    attending = profile.attending.all().filter(
        datetime__gte=today).order_by("datetime")
    attended = profile.attending.all().filter(
        datetime__lt=today).order_by("datetime")
    return render(request, 'registration/my_workshops.html', {"attending": attending, "attended": attended})

#bookmark/remove bookmark stitches
@login_required
def add_bookmark(request, id):
    stitch = get_object_or_404(Stitch, id=id)
    if request.method == "POST":
        request.user.profile.saved.add(stitch)
    return redirect(request.POST.get("redirect_url"))


@login_required
def remove_bookmark(request, id):
    stitch = get_object_or_404(Stitch, id=id)
    if request.method == "POST":
        request.user.profile.saved.remove(stitch)
    return redirect(request.POST.get("redirect_url"))


@login_required
def my_saved_stitches(request):
    today = datetime.today()
    profile = check_if_user_profile(request)

    saved = profile.saved.all().filter()
    return render(request, 'registration/my_saved_stitches.html', {"saved": saved})


###
def learn(request):
    return render(request, 'learn/learn.html')


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


def details(request, title):
    workshop = get_object_or_404(Workshop, title=title)
    print(workshop)
    return render(request, 'learn/details.html', {'workshop': workshop})


def stitch_guide(request):
    filter_map = {
        'stitch': 'stitch__icontains',
    }

    filters = {}
    for key, value in request.GET.items():
        filter_key = filter_map[key]
        filters[filter_key] = value


    stitches = Stitch.objects.filter(**filters).order_by('stitch')
    return render(request, 'learn/stitch_guide.html', {'stitches': stitches})


def the_basics(request):
    filter_map = {
        'title': 'title__icontains',
    }

    filters = {}
    for key, value in request.GET.items():
        filter_key = filter_map[key]
        filters[filter_key] = value


    articles = BasicArticle.objects.filter(**filters)
    return render(request, 'learn/the_basics.html', {'articles': articles})


def basics_details(request, title):
    article = get_object_or_404(BasicArticle, title=title)
    print(article)
    return render(request, 'learn/the_basics_details.html', {'article': article})
