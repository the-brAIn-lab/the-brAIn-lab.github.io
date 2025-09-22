from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("projects/", views.projects, name="projects"),
    path("publications/", views.publications, name="publications"),
    path("software/", views.software, name="software"),
    path("team/", views.team, name="team")
]
