from . import views
from django.urls import path

urlpatterns = [
    path('', views.landing_page, name="landing_page"),
    path('the_club/', views.the_club, name="the_club"),
    path('the_club/members/', views.profile_list, name="profile_list"),
    path('the_club/members/<str:user>/', views.profile, name="profile"),
]