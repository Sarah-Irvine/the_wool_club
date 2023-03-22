from . import views
from django.urls import path

urlpatterns = [
    path('', views.learn, name="learn"),
    path('workshops/', views.list, name="class_list"),
    path('stitch_guide/', views.stitch_guide, name="stitch_guide"),
    path('the_basics/', views.the_basics, name="the_basics"),
    path('workshops/<str:title>/', views.details, name="class_details"),
    path('<int:id>/add_attending/', views.add_attending, name="workshop_add_attending"),
    path('<int:id>/remove_attending/', views.remove_attending, name="workshop_remove_attending"),
    path('my_workshops/', views.my_workshops, name="my_workshops"),
    path('<int:id>/add_bookmark/', views.add_bookmark, name="add_bookmark"),
    path('<int:id>/remove_bookmark/', views.remove_bookmark, name="remove_bookmark"),
    path('my_saved_stitches/', views.my_saved_stitches, name="my_saved_stitches"),
    path('the_basics/<str:title>/', views.basics_details, name="basics_details"),
]