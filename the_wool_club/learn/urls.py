from . import views
from django.urls import path

urlpatterns = [
    path('', views.learn, name="learn"),
    path('workshops/', views.list, name="class_list"),
    path('stitch_guide/', views.stitch_guide, name="stitch_guide"),
    path('the_basics/', views.the_basics, name="the_basics"),
    path('<int:id>/', views.details, name="class_details"),
]