from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from accounts.models import UserProfile
# Create your views here.

def landing_page(request):
    return render(request, 'community/landing_page.html')

def the_club(request):
    return render(request, 'community/the_club.html')

def profile_list(request):
    profiles = UserProfile.objects.exclude(user=request.user)
    return render(request, "community/profile_list.html", {"profiles": profiles})

def profile(request, user):
    profile = {
        "profile" : get_object_or_404(UserProfile, user=user)
    }
    return render(request, "community/profile.html", profile)

def follow(request,user):
    profile = get_object_or_404(UserProfile, user=user)
    if request.method == "POST":
        request.user.profile.follows.add(profile)
    return redirect(request.POST.get("redirect_url"))        

def unfollow(request,user):
    profile = get_object_or_404(UserProfile, user=user)
    if request.method == "POST":
        request.user.profile.follows.remove(profile)
    return redirect(request.POST.get("redirect_url")) 