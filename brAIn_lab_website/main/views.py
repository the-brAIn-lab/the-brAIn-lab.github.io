from django.shortcuts import render

# Create your views here.

def home(response):
    return render(response, "main/home.html", {})

def projects(response):
    return render(response, "main/projects.html", {})

def publications(response):
    return render(response, "main/publications.html", {})

def software(response):
    return render(response, "main/software.html", {})

def team(response):
    return render(response, "main/team.html", {})
