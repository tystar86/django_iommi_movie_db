"""iommi_movie_db URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from base.models import Actor, Category, Country, Director, Movie
from base.views import (
    IndexPage,
    actor_page,
    category_page,
    country_page,
    director_page,
    movie_page,
)
from django.contrib import admin
from django.urls import path
from iommi import Table


urlpatterns = [
    path("", IndexPage().as_view()),
    path("actors/", Table(auto__model=Actor).as_view()),
    path("actors/<id>", actor_page),
    path("directors/", Table(auto__model=Director).as_view()),
    path("directors/<id>", director_page),
    path("movies/", Table(auto__model=Movie).as_view()),
    path("movies/<id>", movie_page),
    path("categories/", Table(auto__model=Category).as_view()),
    path("categories/<id>", category_page),
    path("countries/", Table(auto__model=Country).as_view()),
    path("countries/<id>", country_page),
    path("admin/", admin.site.urls),
]
