from . import views
from django.urls import path

urlpatterns = [
    path('', views.list, name="class_list"),
    path('<int:id>/', views.details, name="class_details"),
]